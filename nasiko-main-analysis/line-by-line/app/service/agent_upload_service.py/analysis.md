# agent_upload_service.py — line-by-line analysis

## Lines 1-8
- Imports OS/path utilities, temp/zip helpers, typing, and YAML support.

## Lines 9-16
- Imports UploadFile and app services/settings; AgentUploadResult class declaration begins.

## Lines 17-24
- AgentUploadResult __init__ parameters for success/name/status and flags.

## Lines 25-32
- Adds upload_id/version params, closes signature, and assigns core fields.

## Lines 33-40
- Stores validation_errors/upload_id/version; defines ValidationResult class and __init__.

## Lines 41-48
- ValidationResult sets errors; _determine_agent_name helper starts and builds Path.

## Lines 49-56
- Looks for docker-compose.yml, parses YAML, and gets services map.

## Lines 57-64
- Returns first container_name, ignores YAML errors, and falls back to directory name.

## Lines 65-72
- Returns basename and starts AgentUploadService __init__ with logger/services.

## Lines 73-80
- Sets agents directory/repository and starts process_zip_upload with docstring.

## Lines 81-88
- Docstring outlines zip upload flow steps.

## Lines 89-96
- Logs upload, initializes temp_dir, and extracts zip to temp directory.

## Lines 97-104
- Auto-detects agent name and validates structure, returning on failure.

## Lines 105-112
- Builds validation failure response and calls _ensure_agentcard_json.

## Lines 113-120
- Ensures AgentCard.json and copies agent to versioned directory.

## Lines 121-128
- Returns success AgentUploadResult and logs exceptions on failure.

## Lines 129-136
- Returns error AgentUploadResult and enters finally for cleanup.

## Lines 137-144
- Removes temp directory and logs warnings on cleanup failure.

## Lines 145-152
- process_directory_upload signature and docstring start.

## Lines 153-160
- Docstring flow and args continue for directory upload.

## Lines 161-168
- Docstring return and logs upload start; begins try block.

## Lines 169-176
- Resolves source_dir and returns directory_not_found error if missing.

## Lines 177-184
- Returns not_directory error when path is not a directory.

## Lines 185-192
- Determines agent name from compose or dir and validates structure.

## Lines 193-200
- Returns validation_failed result when structure check fails.

## Lines 201-208
- Ensures AgentCard.json and copies agent to versioned directory.

## Lines 209-216
- Returns success AgentUploadResult with version and flags.

## Lines 217-224
- Logs directory upload error and returns error result.

## Lines 225-232
- validate_agent_structure signature and docstring describing required files.

## Lines 233-240
- Logs validation start and initializes errors list and agent_dir.

## Lines 241-248
- Checks directory existence and starts Dockerfile validation.

## Lines 249-256
- Handles missing/empty Dockerfile and reads content for checks.

## Lines 257-264
- Validates Dockerfile has FROM and starts docker-compose.yml checks.

## Lines 265-272
- Handles missing compose file or empty content during validation.

## Lines 273-280
- Parses compose YAML and validates services; handles YAML errors.

## Lines 281-288
- Handles compose read errors and defines main.py candidate paths.

## Lines 289-296
- Iterates candidate paths, flags main.py found, and reads content.

## Lines 297-304
- Appends errors for empty/unreadable main.py and breaks loop.

## Lines 305-312
- Adds error when main not found and checks for any Python files.

## Lines 313-320
- Adds error for missing Python files, logs summary, returns ValidationResult.

## Lines 321-328
- _extract_zip_file starts, creates temp dir, logs, reads file content.

## Lines 329-336
- Enforces max size and builds temp zip_path.

## Lines 337-344
- Writes zip file and validates zip integrity.

## Lines 345-352
- Opens zip, checks file count, and starts traversal safety checks.

## Lines 353-360
- Validates paths, extracts files, logs count, removes zip.

## Lines 361-368
- Finds agent directory and returns it; handles exceptions with cleanup.

## Lines 369-376
- Removes temp dir on error, raises ValueError, and starts _find_agent_directory.

## Lines 377-384
- Lists temp contents, filters upload.zip, and checks single-dir case.

## Lines 385-392
- Returns single-dir agent or checks root for agent files.

## Lines 393-400
- Searches multiple dirs for agent files and returns first match.

## Lines 401-408
- Logs fallback and returns temp_dir; starts _ensure_agentcard_json signature.

## Lines 409-416
- Builds AgentCard.json path and returns False if already exists.

## Lines 417-424
- Logs generation intent and enters try to generate AgentCard.

## Lines 425-432
- Calls agentcard_service.generate_and_save_agentcard with base_url.

## Lines 433-440
- Logs success and returns True when AgentCard is generated.

## Lines 441-448
- Logs warnings/errors and returns False on generation failure.

## Lines 449-456
- _get_version_from_agentcard signature and loads AgentCard.json.

## Lines 457-464
- Reads version, adds v-prefix, logs, returns; warns if missing.

## Lines 465-472
- Returns default v1.0.0 and logs warning on exception.

## Lines 473-480
- _copy_to_agents_directory starts and gets version for directory naming.

## Lines 481-488
- Builds target dir, ensures base dir, and removes existing version.

## Lines 489-496
- Copies agent files, logs destination, and returns version.

## Lines 497-503
- __del__ placeholder with TODO for cleanup logic.
