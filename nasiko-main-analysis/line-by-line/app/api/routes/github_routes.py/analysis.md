# github_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for GitHub OAuth and repo endpoints.
- Imports APIRouter, Query, Request, Depends, auth dependency, handler factory, and types.

## Lines 9-16
- Defines create_github_routes factory and router with GitHub tag.
- Starts OAuth login endpoint.

## Lines 17-24
- GET /auth/github/login returns OAuth authorization URL.
- Requires user_id dependency and delegates to handler.

## Lines 25-32
- Defines OAuth callback endpoint metadata.
- Handler accepts code and state query params.

## Lines 33-40
- Delegates callback handling to github handler.
- Defines GET /auth/github/token endpoint.

## Lines 41-48
- get_github_token uses auth dependency and delegates to handler.
- Defines POST /auth/github/logout endpoint.

## Lines 49-56
- github_logout delegates to handler with user_id.
- Starts repository list endpoint.

## Lines 57-64
- GET /github/repositories returns GithubRepositoryListResponse.
- Delegates to list_github_repositories.

## Lines 65-72
- POST /github/clone clones repo and uploads as agent.
- Accepts GithubCloneRequest and user_id.

## Lines 73-80
- Delegates to clone_github_repository.
- Starts public login-user endpoint.

## Lines 81-88
- GET /auth/github/login-user is public and uses shared callback.
- Delegates to github_user_login.

## Lines 89-104
- Returns router.
