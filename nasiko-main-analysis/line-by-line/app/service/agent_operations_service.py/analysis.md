# agent_operations_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for Optional/ObjectId and request types.

## Lines 9-16
- Imports build/deploy entity models, statuses, and settings.

## Lines 17-24
- convert_objectid_to_str helper converts Mongo ObjectId to string.

## Lines 25-32
- AgentOperationsService class and __init__ wiring for repo/K8s/logger.

## Lines 33-40
- trigger_agent_build signature and docstring describing BuildKit flow.

## Lines 41-48
- Enters try, logs build start, and notes optional agent lookup.

## Lines 49-56
- Builds registry URL and image reference for the build.

## Lines 57-64
- Creates AgentBuildBase with queued status and persists build record.

## Lines 65-72
- Raises on missing build record, derives build_id, starts BuildKit job.

## Lines 73-80
- Passes git URL/image destination to K8s build job and checks success.

## Lines 81-88
- Updates build status for success/failure and logs or raises errors.

## Lines 89-96
- Returns build record and handles trigger exceptions with logging.

## Lines 97-104
- deploy_agent_container signature and docstring start.

## Lines 105-112
- Docstring steps and deployment start logging.

## Lines 113-120
- Fetches build record, validates, and extracts image reference.

## Lines 121-128
- Logs image reference and builds deployment record data.

## Lines 129-136
- Persists deployment record and derives deployment ID.

## Lines 137-144
- Builds K8s deployment name and calls deploy_agent.

## Lines 145-152
- Passes image/port/env vars to K8s and prepares DB update.

## Lines 153-160
- Updates deployment status/service_url and logs success.

## Lines 161-168
- Marks deployment failed on K8s failure and raises exception.

## Lines 169-176
- Returns deployment result and handles ValueError/other errors.

## Lines 177-184
- create_build_record_only signature, docstring, and datetime import.

## Lines 185-192
- Builds build_record_data with IDs, version, image, status, logs.

## Lines 193-200
- Adds k8s_job_name/timestamps, creates record, and raises on failure.

## Lines 201-208
- Returns build record and logs errors; update_build_status_only begins.

## Lines 209-216
- Docstring, datetime import, and update_data with status/updated_at.

## Lines 217-224
- Adds optional logs/k8s_job_name/image_reference/error_message fields.

## Lines 225-232
- Updates build record and raises if build_id not found.

## Lines 233-240
- Returns success payload and handles update errors.

## Lines 241-248
- create_deployment_record_only signature/docstring and datetime import.

## Lines 249-256
- Builds deployment_record_data with IDs, status, and service_url.

## Lines 257-264
- Adds k8s deployment name, namespace, timestamps.

## Lines 265-272
- Creates deployment record, raises on failure, and returns result.

## Lines 273-280
- Logs errors and starts update_deployment_status_only.

## Lines 281-288
- Docstring, datetime import, and update_data with status/updated_at.

## Lines 289-296
- Adds optional service_url/k8s_deployment_name/namespace/error_message.

## Lines 297-304
- Updates deployment record and raises when missing.

## Lines 305-312
- Returns success payload and starts exception handling.

## Lines 313-319
- Logs update errors and re-raises exceptions.
