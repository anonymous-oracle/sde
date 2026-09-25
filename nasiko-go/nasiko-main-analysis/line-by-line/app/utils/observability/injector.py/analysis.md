# injector.py — line-by-line analysis

## Lines 1-8
- Imports os, shutil, ast, astor, typing, logging.
- Imports ObservabilityConfig and initializes logger.

## Lines 9-16
- Defines TracingInjector class with docstring.
- Initializes observability source path and config.

## Lines 17-24
- Starts inject_into_agent method with args and return docstring.

## Lines 25-32
- Checks tracing enabled; logs and returns True if disabled.

## Lines 33-40
- Checks injection enabled; logs and returns True if disabled.
- Begins main injection try block.

## Lines 41-48
- Logs start; copies observability module.
- Finds main entry point and injects tracing code.

## Lines 49-56
- Updates dependencies and Dockerfile; logs completion and returns True.

## Lines 57-64
- Handles injection failure with logging and False return.
- Starts _copy_observability_module.

## Lines 65-72
- Creates utils directory and utils/__init__.py if missing.
- Prepares destination for observability module.

## Lines 73-80
- Removes existing dest path if present.
- Defines ignore_patterns to exclude build-time files.

## Lines 81-88
- Copies observability module excluding injector/config.
- Logs copy completion.

## Lines 89-96
- Starts _find_main_file with candidate filenames.
- Checks candidate files at root level.

## Lines 97-104
- Checks candidates under src/ subdirectory.
- Starts fallback search for uvicorn/FastAPI usage.

## Lines 105-112
- Walks all .py files; scans for run patterns.
- Returns first matching file.

## Lines 113-120
- Skips decode/permission errors.
- Raises if no main entry point found.

## Lines 121-128
- Starts _inject_tracing_code; reads source file.
- Parses AST.

## Lines 129-136
- Builds ImportFrom for bootstrap_tracing.
- Reads framework from AgentCard.json.

## Lines 137-144
- Builds bootstrap_tracing call with project_name and optional framework.

## Lines 145-152
- Builds AST call expression.
- Finds last import index.

## Lines 153-160
- Inserts import and bootstrap call after last import.
- Writes modified source via astor.

## Lines 161-168
- Logs injection success.
- Logs and raises on errors.

## Lines 169-176
- Starts _find_last_import_index; scans AST body.
- Returns index of last import.

## Lines 177-184
- Starts _update_requirements; sets req/pyproject paths.
- Retrieves dependencies list.

## Lines 185-192
- Prefers pyproject updates; logs on success.
- Falls back to requirements or creates new file.

## Lines 193-200
- Starts _update_requirements_txt; reads existing content.
- Appends observability deps header and lines.

## Lines 201-208
- Starts _create_requirements_txt; writes deps to new file.

## Lines 209-216
- Starts _update_pyproject_toml; imports toml with fallback.
- If missing, falls back to requirements file.

## Lines 217-224
- Loads pyproject data, ensures project/dependencies keys.

## Lines 225-232
- Builds set of existing dependency names to avoid duplicates.

## Lines 233-240
- Filters new deps not already present.
- Extends dependencies and writes back to file.

## Lines 241-248
- Logs added deps or already present.
- On error, falls back to requirements.

## Lines 249-256
- Logs fallback creation of requirements.txt.
- Starts _update_dockerfile.

## Lines 257-264
- Reads Dockerfile and initializes tracking flags.
- Iterates through lines.

## Lines 265-272
- Detects COPY src/ and inserts COPY utils/ when missing.
- Marks updated_utils.

## Lines 273-280
- Detects RUN pip install and prepares to inject deps.
- Collects multiline pip install commands.

## Lines 281-288
- Gets observability deps; inserts into pip install block.

## Lines 289-296
- Handles multiline pip install: inserts deps before last line.

## Lines 297-304
- Handles single-line pip install by appending deps.
- Marks updated_deps and skips processed lines.

## Lines 305-312
- Writes updated Dockerfile content.
- Logs updates for utils and deps.

## Lines 313-320
- Defines _get_observability_dependencies returning config list.
- Starts _get_agent_framework.

## Lines 321-328
- Computes agent directory and adjusts for src/ structure.
- Builds AgentCard.json path.

## Lines 329-336
- Reads AgentCard.json if present and extracts agentFramework.
- Logs detected framework.

## Lines 337-344
- Logs missing agentFramework or missing AgentCard.json.

## Lines 345-352
- Handles exceptions and returns None.
- Starts validate_injection.

## Lines 353-360
- Validates presence of utils/observability and tracing_utils.py.
- Validates bootstrap_tracing import in main file.

## Lines 361-368
- Returns True on validation success.
- Logs and returns False on errors.

## Lines 369-376
- Defines _get_observability_dependencies and starts agent framework detection.

## Lines 377-384
- Adjusts agent_dir for src/ layout and builds AgentCard.json path.

## Lines 385-392
- Loads AgentCard.json and reads agentFramework field.

## Lines 393-400
- Logs detected framework or missing field; logs when AgentCard.json absent.

## Lines 401-408
- Handles exceptions, returns None, and starts validate_injection.

## Lines 409-416
- Checks observability module and tracing_utils.py exist.

## Lines 417-424
- Reads main file and verifies bootstrap_tracing import.

## Lines 425-431
- Returns True on success; logs validation failure and returns False.
