# agent_upload_tracking_service.py — line-by-line analysis

## Lines 1-8
- Imports os/time/Any/uuid4, UploadStatus, AgentUploadService/Result, and UploadFile.

## Lines 9-16
- Imports settings, declares AgentUploadTrackingService, and begins class docstring.

## Lines 17-24
- Docstring bullets describe tracking/progress; __init__ assigns logger/repository.

## Lines 25-32
- Creates base_service and starts process_zip_upload signature/docstring.

## Lines 33-40
- Initializes start_time/upload_id, reads file content, computes size, resets cursor.

## Lines 41-48
- Determines temp agent name, imports datetime/timezone, and sets current_time.

## Lines 49-56
- Builds initial status_data with ids, owner, status, and progress fields.

## Lines 57-64
- Adds source_info, file_size, status_message, upload_type, and timestamps.

## Lines 65-72
- Creates status record in repository and logs creation.

## Lines 73-80
- Updates status to PROCESSING with progress and message.

## Lines 81-88
- Calls base_service.process_zip_upload and imports OrchestrationService on success.

## Lines 89-96
- Instantiates orchestration and prepares version-aware agent_path.

## Lines 97-104
- Triggers orchestration with agent_name/path/base_url and additional_data.

## Lines 105-112
- Supplies additional_data fields and stores orchestration_triggered on result.

## Lines 113-120
- Updates agent_name if auto-detected and begins success branch.

## Lines 121-128
- Sets progress/status/message defaults and updates for capabilities_generated.

## Lines 129-136
- Updates for orchestration_triggered and calls _update_status with details.

## Lines 137-144
- Failure branch updates status to FAILED with message and validation info.

## Lines 145-152
- Adds processing_duration and closes failure update block.

## Lines 153-160
- Sets upload_id on result, returns, and logs exceptions.

## Lines 161-168
- Updates status to FAILED with unexpected error details and duration.

## Lines 169-176
- Returns AgentUploadResult error payload with upload_id.

## Lines 177-184
- Starts process_github_upload signature and docstring intro.

## Lines 185-192
- Defines args, initializes timing/upload_id, and computes directory size.

## Lines 193-200
- Imports datetime/timezone, sets current_time, and begins GitHub status_data.

## Lines 201-208
- Populates GitHub status_data with ids/status/progress and source_info.

## Lines 209-216
- Adds repo/branch/source_type, file_size, status_message, upload_type, timestamps.

## Lines 217-224
- Creates status record and updates status to PROCESSING.

## Lines 225-232
- Calls base_service.process_directory_upload for GitHub source.

## Lines 233-240
- On success, updates status to CAPABILITIES_GENERATED with agent_name.

## Lines 241-248
- Imports OrchestrationService, instantiates it, and sets versioned agent_path.

## Lines 249-256
- Triggers orchestration with additional_data for owner/upload/repo/branch.

## Lines 257-264
- Stores orchestration_triggered and updates status when triggered.

## Lines 265-272
- Handles orchestration failure and logs processing time.

## Lines 273-280
- Returns result or marks failure with validation_errors.

## Lines 281-288
- Updates FAILED status on error and returns result.

## Lines 289-296
- Logs GitHub upload error, raises, and starts process_directory_upload signature.

## Lines 297-304
- Initializes timing/upload_id, computes directory size, and temp agent name.

## Lines 305-312
- Imports datetime/timezone, sets current_time, and begins status_data.

## Lines 313-320
- Populates status_data for directory uploads with ids/status/progress/source_info.

## Lines 321-328
- Adds file_size/status_message/upload_type/timestamps and enters try block.

## Lines 329-336
- Creates status record and updates status to PROCESSING with message.

## Lines 337-344
- Calls base_service.process_directory_upload and imports OrchestrationService.

## Lines 345-352
- Instantiates orchestration, builds agent_path, and triggers orchestration call.

## Lines 353-360
- Passes additional_data and stores orchestration_triggered; updates agent_name.

## Lines 361-368
- Success branch sets progress/status/message and checks capabilities_generated.

## Lines 369-376
- Completes status_data with file_size/message/type/timestamps before try block.

## Lines 377-384
- Enters try, creates status record, and starts PROCESSING update.

## Lines 385-392
- Sets PROCESSING payload and prepares base_service.process_directory_upload call.

## Lines 393-400
- Calls base_service.process_directory_upload and imports OrchestrationService on success.

## Lines 401-408
- Instantiates orchestration, builds agent_path, and starts trigger call.

## Lines 409-416
- Passes agent_name/path/base_url and additional_data to orchestration trigger.

## Lines 417-424
- Closes trigger call, stores orchestration_triggered, and updates agent_name.

## Lines 425-432
- Sets initial success progress/status/message after auto-detect update.

## Lines 433-440
- Adjusts progress/status/message for capabilities and orchestration flags.

## Lines 441-448
- Sets ORCHESTRATION_TRIGGERED status and starts _update_status payload.

## Lines 449-456
- Finishes success _update_status payload and enters else branch.

## Lines 457-464
- Updates FAILED status with error details, validation errors, and duration.

## Lines 465-472
- Closes failure update, sets upload_id, and returns result.

## Lines 473-480
- Catches exceptions and begins FAILED status update for unexpected errors.

## Lines 481-488
- Completes FAILED status payload with error details and duration.

## Lines 489-496
- Returns AgentUploadResult error payload for directory upload errors.

## Lines 497-504
- Starts _update_status helper with repository update and debug logging.

## Lines 505-512
- Handles _update_status errors and starts _calculate_directory_size helper.

## Lines 513-520
- Begins directory size loop and sums file sizes.

## Lines 521-528
- Returns total size or warns, then starts update_upload_status_by_agent_latest.

## Lines 529-536
- Docstring and repository update call for latest upload status.

## Lines 537-544
- Logs success/returns or warns, then starts exception logging.

## Lines 545-547
- Logs update error and raises exception.
