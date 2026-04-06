# repository.py — line-by-line analysis

## Lines 1-8
- Module docstring indicates a combined repository facade.
- Imports `ObjectId` and repository classes begin.

## Lines 9-16
- Continues imports for repository modules.
- Defines `Repository` class with a descriptive docstring.

## Lines 17-24
- `__init__` stores db/logger.
- Instantiates `registry` and `upload_status` repositories.

## Lines 25-32
- Instantiates `chat`, `n8n`, `github`, and `agent_operations`.
- Declares `ensure_collections` with docstring.

## Lines 33-40
- `ensure_collections` calls `ensure_indexes` for all repos.

## Lines 41-48
- Logs successful index initialization.
- Catches exceptions and logs warnings without failing startup.

## Lines 49-56
- Registry delegation: create/get all/get by id.

## Lines 57-64
- Registry delegation: get by name, get by agent id, update by id.

## Lines 65-72
- Upload status delegation: get by id, create, get by upload id.

## Lines 73-80
- Upload status delegation: update by upload id.
- Begins update by agent name with delegation.

## Lines 81-88
- Completes update by agent name; get by agent name.
- Starts get statuses by user.

## Lines 89-96
- Completes get statuses by user.
- Chat delegation: create session and delete session.

## Lines 97-104
- Chat delegation: get session history.
- Begins get chat history with parameters.

## Lines 105-112
- Completes get chat history delegation.

## Lines 113-120
- N8N delegation: get credential by user id and decrypted version.

## Lines 121-128
- N8N delegation: update and upsert credential.

## Lines 129-136
- N8N delegation: delete and update test result.
- GitHub delegation begins.

## Lines 137-144
- GitHub delegation: get credential, get decrypted, upsert.

## Lines 145-152
- GitHub delegation: delete credential, update test result.

## Lines 153-160
- Agent ops delegation: create build, get build by id.

## Lines 161-168
- Agent ops delegation: update build, create deployment, get deployment.

## Lines 169-176
- Agent ops delegation: update deployment, get builds by agent id.

## Lines 177-184
- Agent ops delegation: get deployments by agent id.
- Begins legacy alias section.

## Lines 185-192
- Legacy delegation: create_build, create_deployment, update_build_status.

## Lines 193-200
- Deletion methods: delete registry, delete builds by agent id.

## Lines 201-208
- Deletion methods: delete deployments and upload status by agent id.

## Line 209
- Returns result of delete_upload_status_by_agent_id.
