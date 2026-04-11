# agent_update_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and base imports for os/time/semver/typing.

## Lines 9-16
- Imports uuid/datetime/UploadFile plus upload/orchestration services.

## Lines 17-24
- Declares AgentUpdateResult and starts __init__ with core fields.

## Lines 25-32
- __init__ parameters continue with version/strategy/status metadata.

## Lines 33-40
- Assigns success, agent/version, and build/deployment fields.

## Lines 41-48
- Stores status/error/upload_id and introduces AgentUpdateService class.

## Lines 49-56
- AgentUpdateService __init__ wires upload/orchestration and imports AgentCardService.

## Lines 57-64
- Instantiates AgentCardService and starts update_agent signature.

## Lines 65-72
- Completes update_agent parameters and opens docstring.

## Lines 73-80
- Docstring lists update args, strategies, and optional description.

## Lines 81-88
- Initializes timing/id, begins try, and loads registry entry.

## Lines 89-96
- Returns failure result when agent not found in registry.

## Lines 97-104
- Computes new version and logs update intent.

## Lines 105-112
- Handles missing file by checking GitHub source and starting handler call.

## Lines 113-120
- Passes all update parameters to GitHub update handler.

## Lines 121-128
- Returns failure if no file and not GitHub-sourced.

## Lines 129-136
- Closes failure return and looks up existing upload record.

## Lines 137-144
- Reuses existing upload record and appends update history.

## Lines 145-152
- Falls back to creating a new update status record.

## Lines 153-160
- Finishes status record creation and sets agent_name.

## Lines 161-168
- Updates status to PROCESSING with 20% progress.

## Lines 169-176
- Calls versioned upload helper with agent/file/version.

## Lines 177-184
- On upload failure, marks status FAILED with error details.

## Lines 185-192
- Returns failure result using upload error status.

## Lines 193-200
- Updates registry with new version metadata.

## Lines 201-208
- Marks status as orchestration-triggered with progress update.

## Lines 209-216
- Starts orchestration trigger call with agent path/base URL.

## Lines 217-224
- Fills orchestration metadata for update action and ownership.

## Lines 225-232
- Closes trigger call and branches on orchestration result.

## Lines 233-240
- Updates status to orchestration processing when triggered.

## Lines 241-248
- Returns success result indicating build underway.

## Lines 249-256
- On trigger failure, marks status failed with message.

## Lines 257-264
- Returns failure result for orchestration trigger issues.

## Lines 265-272
- Starts exception handling and logs update failure.

## Lines 273-280
- Updates status to failed and begins failure return.

## Lines 281-288
- Completes failure return and starts rollback_agent signature.

## Lines 289-296
- Rollback parameters and brief docstring introduction.

## Lines 297-304
- Loads registry entry and returns failure if missing.

## Lines 305-312
- Closes missing-agent return and loads version history.

## Lines 313-320
- Computes active versions list for rollback selection.

## Lines 321-328
- Handles no previous versions and returns rollback failure.

## Lines 329-336
- Selects target version and begins rollback orchestration call.

## Lines 337-344
- Populates rollback orchestration request and metadata.

## Lines 345-352
- Completes rollback trigger call and checks success.

## Lines 353-360
- Updates registry for rollback and returns rolling_back result.

## Lines 361-368
- Returns failure result when rollback trigger fails.

## Lines 369-376
- Handles rollback trigger failure details and closes branch.

## Lines 377-384
- Logs rollback exception and returns failure with fallback version.

## Lines 385-392
- Starts get_version_history and fetches registry entry.

## Lines 393-400
- Builds success payload with current version and history.

## Lines 401-408
- Completes version history response and logs errors on failure.

## Lines 409-416
- Returns error payload and starts _calculate_new_version.

## Lines 417-424
- Normalizes current version and branches on strategy.

## Lines 425-432
- Applies patch/minor/major bumps or parses explicit version.

## Lines 433-440
- Logs version calc failure and begins semantic fallback.

## Lines 441-448
- Strips v-prefix and validates semantic version format.

## Lines 449-456
- Bumps patch or falls back to 1.0.1 with warning.

## Lines 457-464
- Starts _process_versioned_upload and imports temp helpers.

## Lines 465-472
- Creates versioned directory and prepares temp workspace.

## Lines 473-480
- Processes zip upload into temporary agent directory.

## Lines 481-488
- On success, locates temp agent path and logs copy start.

## Lines 489-496
- Builds list of versioned subdirectories in temp output.

## Lines 497-504
- Chooses first versioned subdir when present.

## Lines 505-512
- Sets source_path from subdir or temp root and logs.

## Lines 513-520
- Begins copy loop over processed agent files.

## Lines 521-528
- Copies directories, removing existing destinations first.

## Lines 529-536
- Copies files, logs, and raises on copy errors.

## Lines 537-544
- Ensures AgentCard.json exists and starts version validation.

## Lines 545-552
- Warns on AgentCard version mismatch but continues.

## Lines 553-560
- Cleans temp agent dir and updates result paths.

## Lines 561-568
- Handles missing temp path and enters exception handling.

## Lines 569-576
- Marks result failed when temp agent dir missing.

## Lines 577-584
- Returns AgentUploadResult failure on processing exceptions.

## Lines 585-592
- Starts _process_versioned_github_upload helper.

## Lines 593-600
- Creates versioned dir and processes GitHub upload in temp.

## Lines 601-608
- On success, sets temp agent path and logs copy start.

## Lines 609-616
- Notes nested version folder handling for GitHub flow.

## Lines 617-624
- Builds list of versioned subdirectories from temp output.

## Lines 625-632
- Chooses source_path when versioned subdir exists.

## Lines 633-640
- Uses temp root when no versioned subdir found.

## Lines 641-648
- Copies directories to versioned path for GitHub update.

## Lines 649-656
- Copies files and logs per-item success.

## Lines 657-664
- Logs copy errors and ensures AgentCard.json.

## Lines 665-672
- Ensures AgentCard.json and removes temp agent directory.

## Lines 673-680
- Updates result paths or logs missing temp directory.

## Lines 681-688
- Returns failure for missing temp agent dir and starts exception path.

## Lines 689-696
- Logs GitHub upload failure and returns AgentUploadResult error.

## Lines 697-704
- Closes error return and starts _find_existing_upload_record.

## Lines 705-712
- Scans upload records for completed/orchestration entries.

## Lines 713-720
- Returns upload_id or logs lookup error on failure.

## Lines 721-728
- Starts _add_update_to_existing_record signature.

## Lines 729-736
- Loads existing upload record and handles missing case.

## Lines 737-744
- Initializes upload_history and prepares new update entry.

## Lines 745-752
- Fills new update record fields for history.

## Lines 753-760
- Appends update and begins update_data dict.

## Lines 761-768
- Updates upload status record and logs completion.

## Lines 769-776
- Logs errors and starts _create_update_status_record.

## Lines 777-784
- Sets parameters and begins status record creation.

## Lines 785-792
- Builds status_data with base metadata and progress fields.

## Lines 793-800
- Starts upload_history entry for new version.

## Lines 801-808
- Completes history entry and starts source_info metadata.

## Lines 809-816
- Finishes status_data with source info, messages, and timestamps.

## Lines 817-824
- Creates upload status record and starts _update_status helper.

## Lines 825-832
- Updates status with timestamp, logs errors, begins _update_registry_version.

## Lines 833-840
- Defines _update_registry_version parameters and starts try block.

## Lines 841-848
- Fetches registry entry and exits if missing.

## Lines 849-856
- Loads version history and marks previous version archived.

## Lines 857-864
- Builds new_version_info with building status and build IDs.

## Lines 865-872
- Completes new_version_info with rollback info and appends history.

## Lines 873-880
- Prepares registry update_data with new version and history.

## Lines 881-888
- Updates registry by ObjectId and logs success.

## Lines 889-896
- Logs update errors and starts _update_registry_rollback.

## Lines 897-904
- Defines rollback update params and loads registry entry.

## Lines 905-912
- Marks current version as failed in history.

## Lines 913-920
- Records rollback reason and marks target version active.

## Lines 921-928
- Builds rollback update_data and imports ObjectId.

## Lines 929-936
- Updates registry for rollback and logs completion.

## Lines 937-944
- Logs rollback update errors and starts _get_agent_original_source.

## Lines 945-952
- Fetches upload records to find original source.

## Lines 953-960
- Returns first successful upload record or logs missing.

## Lines 961-968
- Handles lookup errors and returns None.

## Lines 969-976
- Starts GitHub update handler signature after error logging.

## Lines 977-984
- Completes GitHub update parameters and enters try block.

## Lines 985-992
- Logs GitHub update and loads registry entry.

## Lines 993-1000
- Returns failure when registry entry is missing.

## Lines 1001-1008
- Derives agent_name and extracts repo/branch from source info.

## Lines 1009-1016
- Returns failure if GitHub repository info is missing.

## Lines 1017-1024
- Starts reuse/create upload record logic for GitHub updates.

## Lines 1025-1032
- Reuses existing upload record and appends update history.

## Lines 1033-1040
- Falls back to creating a new update status record.

## Lines 1041-1048
- Finalizes record creation and updates status to cloning.

## Lines 1049-1056
- Sets PROCESSING status with GitHub clone message.

## Lines 1057-1064
- Instantiates GitHubService and fetches user credentials.

## Lines 1065-1072
- Returns failure when GitHub credentials are missing.

## Lines 1073-1080
- Extracts access token and starts repository clone.

## Lines 1081-1088
- Processes cloned repo and sets up cleanup in finally.

## Lines 1089-1096
- Removes temp clone directory and logs cleanup.

## Lines 1097-1104
- Updates status on GitHub upload failure.

## Lines 1105-1112
- Returns failure result for GitHub upload errors.

## Lines 1113-1120
- Updates registry with new version after GitHub upload.

## Lines 1121-1128
- Marks status as orchestration-triggered for GitHub update.

## Lines 1129-1136
- Starts orchestration trigger for GitHub update.

## Lines 1137-1144
- Adds update metadata to GitHub orchestration request.

## Lines 1145-1152
- Adds repo/branch info and closes orchestration call.

## Lines 1153-1160
- Updates status to orchestration processing on success.

## Lines 1161-1168
- Returns success result for GitHub update build.

## Lines 1169-1176
- Begins failure branch and updates status on trigger failure.

## Lines 1177-1184
- Returns failure result for orchestration trigger errors.

## Lines 1185-1192
- Logs exception and prepares failure handling for GitHub update.

## Lines 1193-1200
- Updates status to failed on GitHub update exception.

## Lines 1201-1208
- Returns GitHub update failure result with error message.

## Lines 1209-1216
- Starts _validate_agentcard_version and opens try block.

## Lines 1217-1224
- Loads AgentCard.json and returns warning when missing.

## Lines 1225-1232
- Returns warning when AgentCard has no version field.

## Lines 1233-1240
- Normalizes versions by stripping v-prefix for comparison.

## Lines 1241-1248
- Returns success payload when versions match.

## Lines 1249-1256
- Returns mismatch payload when versions differ.

## Lines 1257-1264
- Returns validation error payload on exception.

