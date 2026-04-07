# github_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring for GitHub handler.
- Imports HTTPException/status/Request, HTMLResponse, BaseHandler, types, GitHubService.

## Lines 9-16
- Defines GitHubHandler and __init__.
- Initializes GitHubService.

## Lines 17-24
- github_login logs and gets auth URL from service.
- Handles missing client ID as 503.

## Lines 25-32
- github_callback resolves OAuth state and flow.
- For connect flow: handles callback and returns HTML response.

## Lines 33-40
- For login flow: returns token/username flags or raises 400.
- Rejects unsupported flow.

## Lines 41-48
- get_github_access_token handles status mapping.
- Returns 202 for not_connected/token_expired/invalid_credential.

## Lines 49-56
- Returns 500 on error statuses or unknown statuses.
- github_logout delegates to service.

## Lines 57-64
- list_github_repositories delegates to service and wraps response.
- clone_github_repository logs and calls service.

## Lines 65-72
- Builds AgentUploadResponse from service result.
- Handles errors via handle_service_error.

## Lines 73-80
- github_user_login delegates to get_github_auth_url_for_login.
- Handles ValueError as 503.
