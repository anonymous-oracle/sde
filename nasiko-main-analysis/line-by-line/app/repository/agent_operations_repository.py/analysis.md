# agent_operations_repository.py — line-by-line analysis

## Lines 1-8
- Module docstring describes agent build/deployment repository.
- Imports `ObjectId`, datetime helpers, and base repository.

## Lines 9-16
- Defines `AgentOperationsRepository` and constructor.
- Sets Mongo collections for builds and deployments.

## Lines 17-24
- `ensure_indexes` starts; creates build collection indexes.
- Indexes on `agent_id`, `github_url`, `status`, timestamps.

## Lines 25-32
- Adds deployment collection indexes (agent_id, build_id, status).
- Adds namespace and created_at indexes.

## Lines 33-40
- Logs successful index creation or warns on error.

## Lines 41-48
- `create_agent_build` inserts a build and returns it.
- `get_agent_build_by_id` fetches a build by `_id`.

## Lines 49-56
- `update_agent_build` stamps `updated_at` and updates.
- `get_agent_builds_by_agent_id` begins query by agent.

## Lines 57-64
- Sorts builds by `created_at` descending and limits results.
- Returns list with configured limit.

## Lines 65-72
- `get_agent_builds_by_status` queries by status, sorts, limits.
- Returns list for monitoring.

## Lines 73-80
- `create_agent_deployment` inserts and returns deployment doc.
- `get_agent_deployment_by_id` fetches by `_id`.

## Lines 81-88
- `update_agent_deployment` stamps `updated_at` and updates.
- Returns updated deployment.

## Lines 89-96
- `get_agent_deployments_by_agent_id` queries by agent, sorts, limits.
- Returns list of deployments.

## Lines 97-104
- `get_agent_deployment_by_build_id` fetches deployment by build.
- `get_active_deployments` begins active deployment query.

## Lines 105-112
- Returns deployments in namespace with status in starting/running.
- Adds legacy alias `create_build`.

## Lines 113-120
- `create_deployment` legacy method returns string ID.
- `update_build_status` begins status update helper.

## Lines 121-128
- Builds update payload, includes logs if provided.
- Updates build status by `_id`.

## Lines 129-136
- `delete_agent_builds_by_agent_id` deletes many build records.
- Logs deletion count and returns it.

## Lines 137-144
- Logs and returns 0 on delete failure for builds.
- `delete_agent_deployments_by_agent_id` begins.

## Lines 145-152
- Deletes deployment records; logs count and returns it.

## Lines 153-160
- Logs and returns 0 on deployment deletion failure.
