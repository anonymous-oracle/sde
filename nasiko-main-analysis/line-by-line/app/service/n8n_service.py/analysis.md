# n8n_service.py — line-by-line analysis

## Lines 1-8
- Imports httpx/shutil/json/base64/os, typing, datetime, and Path utilities.

## Lines 9-16
- Imports N8nRegisterRequest and defines N8nService class with __init__ signature.

## Lines 17-24
- Stores base_url/api_key/logger and builds default headers dict.

## Lines 25-32
- test_connection starts, uses AsyncClient, calls workflows endpoint with limit.

## Lines 33-40
- Handles 200 response and builds success payload with instance_info.

## Lines 41-48
- Calculates total_workflows count from response shape.

## Lines 49-56
- Handles 401 invalid key and returns failure payload.

## Lines 57-64
- Handles 403 forbidden response and returns failure payload.

## Lines 65-72
- Handles other status codes and returns connection failure message.

## Lines 73-80
- Handles connect/timeout exceptions with error messages.

## Lines 81-88
- Logs generic error and returns failure payload.

## Lines 89-96
- get_workflows signature/docstring and AsyncClient GET call.

## Lines 97-104
- Parses 200 response and handles dict/list response shapes.

## Lines 105-112
- Normalizes workflows via _normalize_workflow_data.

## Lines 113-120
- Returns normalized workflows; logs error on non-200 response.

## Lines 121-128
- Handles exceptions; get_workflow_by_id signature begins.

## Lines 129-136
- Calls workflow by ID endpoint and returns normalized data on 200.

## Lines 137-144
- Logs errors on failure and returns None.

## Lines 145-152
- extract_webhook_id scans nodes for chatTrigger and returns webhookId.

## Lines 153-160
- is_chat_workflow checks for chatTrigger node and returns boolean.

## Lines 161-168
- get_executions signature and builds query params.

## Lines 169-176
- Calls executions endpoint with params and headers.

## Lines 177-184
- Parses response data for dict/list shapes.

## Lines 185-192
- Normalizes execution data with _normalize_execution_data.

## Lines 193-200
- Returns normalized executions or logs non-200 error.

## Lines 201-208
- Handles exceptions and returns empty list.

## Lines 209-216
- get_execution_by_id signature and params for includeData.

## Lines 217-224
- Calls execution endpoint, returns normalized data on 200.

## Lines 225-232
- Logs errors and returns None on failure/exception.

## Lines 233-240
- _normalize_workflow_data begins, checks chat trigger and webhook_id.

## Lines 241-248
- Builds normalized workflow fields: id/name/active/tags/nodes/connections/settings.

## Lines 249-256
- Adds staticData, timestamps, versionId, meta, nodes_count, chat flags.

## Lines 257-264
- Builds chat_url and includes raw_data in normalized output.

## Lines 265-272
- _normalize_execution_data starts and extracts start/finish timestamps.

## Lines 273-280
- Parses started_at string/epoch into datetime.

## Lines 281-288
- Parses finished_at string/epoch into datetime.

## Lines 289-296
- Computes duration_ms and handles parse exceptions.

## Lines 297-304
- Determines execution status based on finished/error flags.

## Lines 305-312
- Builds normalized execution payload with ids, status, times, and error info.

## Lines 313-320
- Adds data/retry fields and raw_data to execution payload.

## Lines 321-328
- register_workflow_as_agent signature and docstring start.

## Lines 329-336
- Fetches workflow by ID and returns error if missing.

## Lines 337-344
- Extracts webhook_id and sets workflow_name as agent_name.

## Lines 345-352
- Normalizes workflow_name, trims length, and builds agent_id components.

## Lines 353-360
- Removes non-alphanumeric chars and constructs agent_id with workflow/user IDs.

## Lines 361-368
- Checks registry for existing agent name and returns error if exists.

## Lines 369-376
- Sets container/folder name and constructs webhook_url.

## Lines 377-384
- Appends /chat for chat workflows and starts _create_a2a_webhook_agent call.

## Lines 385-392
- Handles agent creation failure and returns error message.

## Lines 393-400
- Retrieves generated AgentCard and errors if missing.

## Lines 401-408
- Builds registry_data using AgentCard with id/name/owner and metadata.

## Lines 409-416
- Adds metadata fields, created/updated timestamps to registry_data.

## Lines 417-424
- Creates registry entry and starts upload tracking entry data.

## Lines 425-432
- Builds upload_data with source_info and status details.

## Lines 433-440
- Adds metadata and timestamps for upload_data and writes status record.

## Lines 441-448
- Initializes OrchestrationService and triggers orchestration command.

## Lines 449-456
- Supplies orchestration additional_data and handles trigger response.

## Lines 457-464
- Updates upload status to PROCESSING when orchestration triggered.

## Lines 465-472
- Returns success response with agent info and orchestration status.

## Lines 473-480
- Logs registration errors and returns failure payload.

## Lines 481-488
- _create_a2a_webhook_agent signature and docstring.

## Lines 489-496
- Defines template/target dirs and validates template existence.

## Lines 497-504
- Creates target dir and copies template files.

## Lines 505-512
- Builds docker-compose.yml content with webhook/user info and networks.

## Lines 513-520
- Writes compose file and starts workflow JSON handling.

## Lines 521-528
- Writes n8n_workflow.json and logs saved workflow data.

## Lines 529-536
- Initializes agentcard_generator for n8n and starts generation.

## Lines 537-544
- Generates AgentCard, writes AgentCard.json, logs success.

## Lines 545-552
- Handles AgentCard generation failures with errors/raises.

## Lines 553-560
- Writes compose file and begins workflow JSON save/generation block.

## Lines 561-568
- Saves n8n_workflow.json with raw workflow data and logs location.

## Lines 569-576
- Imports AgentCardGeneratorAgent and initializes generator for n8n.

## Lines 577-584
- Generates agent card and begins success handling.

## Lines 585-592
- Writes AgentCard.json and logs success when generation succeeds.

## Lines 593-600
- Logs generation failure, raises exception, and handles error case.

## Lines 601-608
- Logs generator errors, raises, and handles missing workflow_data case.

## Lines 609-616
- Logs created agent structure and begins success return payload.

## Lines 617-624
- Returns success payload and handles exceptions with error return.

## Lines 625-632
- Begins credential utilities and decrypt_credentials base64 decode.

## Lines 633-640
- Handles decrypt failure and starts encrypt_credentials.

## Lines 641-648
- Encodes credentials and starts get_execution_traces.

## Lines 649-656
- Fetches execution details and returns empty when missing.

## Lines 657-664
- Initializes traces list and iterates runData by node/run.

## Lines 665-672
- Builds trace dict for each output item with metadata fields.

## Lines 673-680
- Appends traces and returns list.

## Lines 681-688
- Logs trace extraction errors and returns empty list.

## Lines 689-689
- Ends file after error handling.
