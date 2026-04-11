# agent_builder.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for temp dirs, file ops, and YAML.

## Lines 9-16
- Imports logging/asyncio/Path and orchestration helpers/constants.

## Lines 17-24
- Initializes logger, defines AgentBuilder class, sets agents dir.

## Lines 25-32
- Creates registry/injector instances and begins batch build method.

## Lines 33-40
- Validates agents directory, initializes counters, iterates folders.

## Lines 41-48
- Increments totals, builds each agent, logs summary success rate.

## Lines 49-56
- build_single_agent resolves folder and validates existence.

## Lines 57-64
- Validates agent structure and logs build start.

## Lines 65-72
- Copies agent into temp dir and builds instrumented image.

## Lines 73-80
- Checks build success, deploys agent, then prepares registry update.

## Lines 81-88
- Updates registry, cleans temp dir, evaluates registry success.

## Lines 89-96
- Logs registry success or warning details for agent.

## Lines 97-104
- Returns success or logs exception; starts async build/deploy API.

## Lines 105-112
- build_and_deploy_agent signature, defaults, and docstring header.

## Lines 113-120
- Docstring describes args and return structure.

## Lines 121-128
- Logs start, resolves agent path, validates existence.

## Lines 129-136
- Returns error dict for missing path and validates structure.

## Lines 137-144
- Returns error for invalid structure and prepares executor call.

## Lines 145-152
- Runs sync build in executor and returns result or logs error.

## Lines 153-160
- Returns failure dict and defines _build_agent_sync.

## Lines 161-168
- Creates temp dir, copies agent, and builds image.

## Lines 169-176
- Handles build failure cleanup and deploy failure cleanup.

## Lines 177-184
- Updates registry and cleans temp directory.

## Lines 185-192
- Builds agent URL and initializes result fields.

## Lines 193-200
- Completes result dict and logs successful registration.

## Lines 201-208
- Logs URL/registry ID or warns on registry failure.

## Lines 209-216
- Adds warning for registry failure and returns result.

## Lines 217-224
- Handles sync build exceptions and returns error dict.

## Lines 225-232
- _validate_agent_structure checks docker-compose presence.

## Lines 233-240
- Loads compose YAML and validates services section.

## Lines 241-248
- Errors on missing services and prepares container names list.

## Lines 249-256
- Collects container names and enforces folder-name match.

## Lines 257-264
- Logs structure validation success and returns True.

## Lines 265-272
- Handles compose parse errors and returns False.

## Lines 273-280
- _build_instrumented_image checks Dockerfile and logs errors.

## Lines 281-288
- Attempts image inspect for cached image reuse.

## Lines 289-296
- Reuses cached image or logs intent to build new image.

## Lines 297-304
- Re-checks cache then logs build start.

## Lines 305-312
- Reads Dockerfile and begins instrumentation install snippet.

## Lines 313-320
- Lists OpenTelemetry packages for instrumentation install.

## Lines 321-328
- Continues package list and sets ROOT_PATH env.

## Lines 329-336
- Appends instrumentation to Dockerfile and writes file.

## Lines 337-344
- Prepares docker build process and imports subprocess.

## Lines 345-352
- Launches docker build subprocess with streamed output.

## Lines 353-360
- Streams build output, prints lines, collects output.

## Lines 361-368
- Checks return code and logs success or failure.

## Lines 369-376
- Logs errors and last output lines on build failure.

## Lines 377-384
- Handles build exceptions and returns False.

## Lines 385-392
- _deploy_agent checks compose file and logs missing file errors.

## Lines 393-400
- Loads compose YAML and ensures networks section exists.

## Lines 401-408
- Adds external agents network configuration.

## Lines 409-416
- Normalizes service network lists and converts dicts.

## Lines 417-424
- Ensures agents network attached and sets image tag.

## Lines 425-432
- Replaces build with image and writes updated compose file.

## Lines 433-440
- Builds docker compose command and prepares env file usage.

## Lines 441-448
- Adds env-file if present and runs docker compose up.

## Lines 449-456
- Logs deploy success or error and returns status.

## Lines 457-464
- Logs return code/stdout/stderr on failure.

## Lines 465-466
- Handles deploy exceptions and returns False.
