# agent_operations_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring for agent build/deploy handler.
- Imports HTTPException/status, BaseHandler, request types, and response models.

## Lines 9-16
- Imports AgentOperationsService and K8sService.
- Defines AgentOperationsHandler class and __init__.

## Lines 17-24
- Initializes K8sService and AgentOperationsService.
- create_build_record signature begins.

## Lines 25-32
- Logs build creation and delegates to service.create_build_record_only.
- Returns result or raises 500 on failure.

## Lines 33-40
- update_build_status logs and delegates to update_build_status_only.
- Handles invalid build_id with 400.

## Lines 41-48
- Handles errors with 500 response.
- create_deployment_record signature begins.

## Lines 49-56
- Logs deployment record creation and delegates to service.
- Returns result or raises 500 on error.

## Lines 57-64
- update_deployment_status logs and delegates to update_deployment_status_only.
- Handles invalid deployment ID with 400.

## Lines 65-72
- Handles errors with 500.
- get_version_mapping signature begins.

## Lines 73-80
- Logs mapping lookup and delegates to service.
- Raises 404 if mapping not found.

## Lines 81-88
- Builds VersionMappingResponse and returns.
- Handles errors with 500.
