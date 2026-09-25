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

## Lines 81-88
- Logs token status request, calls service, reads status and success flags.

## Lines 89-96
- Returns result when connected; raises 202 for not_connected.

## Lines 97-104
- Raises 202 for token_expired with pending message.

## Lines 105-112
- Raises 202 for invalid_credential to avoid client logout.

## Lines 113-120
- Raises 500 for error/unknown status cases.

## Lines 121-128
- Re-raises HTTPException and handles errors via handle_service_error.

## Lines 129-136
- github_logout logs request, calls service, handles exceptions.

## Lines 137-144
- Handles logout errors with handle_service_error.

## Lines 145-152
- list_github_repositories logs and calls service for repo list.

## Lines 153-160
- Wraps repositories into GithubRepositoryListResponse or errors.

## Lines 161-168
- clone_github_repository logs request and calls clone service.

## Lines 169-176
- Builds agent_upload_data from service result.

## Lines 177-184
- Returns AgentUploadResponse with success/failure message.

## Lines 185-192
- Handles clone errors via handle_service_error.

## Lines 193-200
- github_user_login logs and returns auth_url from service.

## Lines 201-208
- Raises 503 on ValueError from missing OAuth config.

## Lines 209-213
- Handles login errors with handle_service_error.
