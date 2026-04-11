# images_group.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for JSON/subprocess/dataclasses.

## Lines 9-16
- Imports Path/typing/typer/Rich helpers and initializes console.

## Lines 17-24
- Defines Typer command group and ImageSpec dataclass with dockerfile.

## Lines 25-32
- Adds ImageSpec context/aliases and starts SERVICES map.

## Lines 33-40
- Defines router and registry image specs with aliases.

## Lines 41-48
- Defines chat history and auth image specs.

## Lines 49-56
- Adds auth alias and k8s build worker image entry.

## Lines 57-64
- Adds orchestrator/web/auth-oss images and closes SERVICES map.

## Lines 65-72
- get_project_root resolves repo root and documents expected layout.

## Lines 73-80
- Validates core/web dirs and starts _resolve_services.

## Lines 81-88
- Builds alias mapping for resolving service filters.

## Lines 89-96
- Validates requested services and errors on unknown names.

## Lines 97-104
- Builds resolved service dict and starts docker login helper.

## Lines 105-112
- Reads Docker config JSON and inspects auths.

## Lines 113-120
- Checks for Docker Hub login and ignores parse errors.

## Lines 121-128
- Prompts docker login and exits on failure.

## Lines 129-136
- _ensure_buildx verifies buildx availability.

## Lines 137-144
- Reports missing buildx and checks for buildx builder.

## Lines 145-152
- Creates builder if missing; errors on failure.

## Lines 153-160
- Activates builder and returns builder name.

## Lines 161-168
- Uses buildx builder and returns builder name.

## Lines 169-176
- _build_images signature and initial setup with platform detection.

## Lines 177-184
- Ensures buildx for multi-platform and prepares images list.

## Lines 185-192
- Resolves Dockerfile/context paths and handles missing file.

## Lines 193-200
- Builds buildx command with platform and image tags.

## Lines 201-208
- Handles multi-platform push behavior and emits warnings.

## Lines 209-216
- Continues warnings and starts single-platform build command.

## Lines 217-224
- Builds single-platform docker build command and tags.

## Lines 225-232
- Applies no-cache, adds context path.

## Lines 233-240
- Handles dry run or executes build and logs progress.

## Lines 241-248
- Handles build failures or success per image.

## Lines 249-256
- Returns build success flag and starts _push_images.

## Lines 257-264
- Initializes push success and iterates services/images.

## Lines 265-272
- Builds docker push commands for each image.

## Lines 273-280
- Handles dry-run output or executes push.

## Lines 281-288
- Logs push success or failure and returns status.

## Lines 289-296
- build_cmd options for username/tag/service filters.

## Lines 297-304
- build_cmd options for platform/multi/no-cache/dry-run.

## Lines 305-312
- build_cmd docstring and resolves service list.

## Lines 313-320
- Overrides platform for multi-platform and prints summary.

## Lines 321-328
- Prints target platform and checks docker availability.

## Lines 329-336
- Exits if docker unavailable and kicks off build.

## Lines 337-344
- Handles build failure and prints completion message.

## Lines 345-352
- Starts push_cmd and username/tag options.

## Lines 353-360
- Adds service filter options for push_cmd.

## Lines 361-368
- Adds dry-run option and begins push_cmd body.

## Lines 369-376
- Resolves services and prints push summary.

## Lines 377-384
- Ensures docker login, pushes images, and handles failure.

## Lines 385-392
- Prints push success and starts build-push command.

## Lines 393-400
- build_push_cmd options for username/tag/service.

## Lines 401-408
- build_push_cmd options for platform/multi/no-cache.

## Lines 409-416
- Adds dry-run option, resolves services, handles multi-platform.

## Lines 417-424
- Prints summary, checks docker, and logs into registry.

## Lines 425-432
- Runs multi-platform build+push or prepares single-platform path.

## Lines 433-440
- Executes single-platform build and handles failure.

## Lines 441-448
- Runs push for single-platform build and handles failure.

## Lines 449-456
- Prints build+push success message.

## Lines 457-464
- Starts list_cmd and builds service table columns.

## Lines 465-472
- Adds tag column and iterates services to populate rows.

## Lines 473-478
- Renders table output.
