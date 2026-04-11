# agent_operations_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for agent build/deploy endpoints.
- Imports APIRouter, Query, HandlerFactory, and request/response types.

## Lines 9-16
- Imports AgentBuildInDB and AgentDeploymentBase models.
- Defines create_agent_operations_routes factory.

## Lines 17-24
- Creates router with prefix `/agents` and tags.
- Declares POST /build endpoint with response model and metadata.

## Lines 25-32
- create_build_record handler delegates to handler factory.
- Declares POST /deploy endpoint with response model and metadata.

## Lines 33-40
- create_deployment_record handler delegates to handler factory.
- Declares PUT /build/{build_id}/status endpoint.

## Lines 41-48
- update_build_status handler delegates to handler factory.
- Declares PUT /deployment/{deployment_id}/status endpoint.

## Lines 49-56
- update_deployment_status handler delegates to handler factory.
- Declares GET /build/version-mapping endpoint with response model.

## Lines 57-64
- get_version_mapping reads agent_id and semantic_version from query params.
- Delegates to handler factory and returns router.

## Lines 65-72
- Declares /build/version-mapping route metadata and handler signature.

## Lines 73-80
- Delegates to handler for version mapping and returns router.
