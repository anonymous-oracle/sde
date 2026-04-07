# agent_upload_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for agent upload and status endpoints.
- Imports FastAPI helpers, handler factory, and response/request types.

## Lines 9-16
- Imports auth dependency and Optional typing.
- Defines create_agent_upload_routes factory.

## Lines 17-24
- Creates router and defines POST /agents/upload endpoint.
- upload_agent_zip accepts file, optional agent_name, user_id.

## Lines 25-32
- Delegates to handlers.agent_upload.upload_agent_zip.
- Sets response status_code from result.

## Lines 33-40
- Defines POST /agents/upload-directory endpoint.
- upload_agent_directory accepts directory path and user_id.

## Lines 41-48
- Delegates to upload_agent_directory handler.
- Sets response status_code and returns result.

## Lines 49-56
- Defines PUT /upload-status/agent/{agent_name}/latest endpoint.
- Delegates to update_upload_status_by_agent_latest.

## Lines 57-64
- Defines GET /user/upload-agents endpoint with limit and user_id.
- Delegates to get_user_upload_agents (prints user_id).

## Lines 65-72
- Defines GET /agents/{agent_name}/download endpoint for BuildKit.
- Accepts optional version query param and delegates to download_agent_files.

## Lines 73-98
- Returns router.
