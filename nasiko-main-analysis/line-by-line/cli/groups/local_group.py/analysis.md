# local_group.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for os/subprocess/time.

## Lines 9-16
- Imports Path/typing and Rich UI helpers for CLI output.

## Lines 17-24
- Initializes console, Typer group, and compose file constant.

## Lines 25-32
- Defines project name and begins _get_project_root.

## Lines 33-40
- Verifies compose file exists or raises error; starts docker check.

## Lines 41-48
- Runs docker ps to verify daemon; handles not running/install errors.

## Lines 49-56
- Handles missing docker/timeout and starts compose availability check.

## Lines 57-64
- Runs docker compose version and handles missing plugin.

## Lines 65-72
- Prints compose errors and exits on failures.

## Lines 73-80
- _check_port_availability uses socket to check port binding.

## Lines 81-88
- Returns availability and defines _compose_cmd helper.

## Lines 89-96
- Builds docker compose command with file and project name.

## Lines 97-104
- Runs compose command and defines _compose_cmd_silent.

## Lines 105-112
- Builds silent compose command and executes with captured output.

## Lines 113-120
- Defines _load_env_file and lists possible env files.

## Lines 121-128
- Loads first env file found via python-dotenv.

## Lines 129-136
- Ends _load_env_file and starts PORT_DEFAULTS mapping.

## Lines 137-144
- Defines default ports for Mongo/Redis/Kong services.

## Lines 145-152
- Adds defaults for backend/auth/router/chat/web and telemetry ports.

## Lines 153-160
- Adds Langtrace/ClickHouse ports and closes defaults.

## Lines 161-168
- Defines _get_port helper; commented _wait_for_service starts.

## Lines 169-176
- Commented-out service wait logic (loop and curl).

## Lines 177-184
- Commented-out wait function end and local_up command decorator.

## Lines 185-192
- local_up options and docstring for starting stack.

## Lines 193-200
- Ensures docker/compose, loads env, and prepares port checks.

## Lines 201-208
- Builds critical ports map and unavailable list.

## Lines 209-216
- Warns on port conflicts and confirms continuation.

## Lines 217-224
- Prints startup messages and begins stale container removal.

## Lines 225-232
- Reads compose config and extracts container names.

## Lines 233-240
- Removes stale containers and begins image build.

## Lines 241-248
- Builds images and warns on build failures.

## Lines 249-256
- Builds compose up args, handles detach, starts services.

## Lines 257-264
- Prints success/waiting messages when detached.

## Lines 265-272
- Uses Live spinner to simulate health checks.

## Lines 273-280
- Updates spinner and prints stack-ready header.

## Lines 281-288
- Creates services table, adds columns, Kong/Backend rows.

## Lines 289-296
- Adds Konga and Service Registry rows.

## Lines 297-304
- Adds Router and Auth Service rows.

## Lines 305-312
- Adds Chat History/Web UI rows and prints table.

## Lines 313-320
- Prints quick command list header and entries.

## Lines 321-328
- Prints deploy/stop commands and first-steps header.

## Lines 329-336
- Prints first steps URLs and spacing.

## Lines 337-344
- Handles FileNotFound/KeyboardInterrupt for local_up.

## Lines 345-352
- Defines local_down command and volume option.

## Lines 353-360
- Ensures docker/compose and confirms volume deletion.

## Lines 361-368
- Runs compose down (with/without volumes) and prints success.

## Lines 369-376
- Handles KeyboardInterrupt and starts local_status command.

## Lines 377-384
- Runs compose ps and prints status or warning.

## Lines 385-392
- Handles errors and defines local_logs command.

## Lines 393-400
- local_logs arguments for service/follow/lines.

## Lines 401-408
- Builds compose logs args and handles follow flag.

## Lines 409-416
- Appends service args and runs compose logs.

## Lines 417-424
- Handles KeyboardInterrupt and starts local_deploy_agent command.

## Lines 425-432
- local_deploy_agent parameters for agent name/path.

## Lines 433-440
- Imports requests, sets default agent path, resolves path.

## Lines 441-448
- Validates path and docker-compose file, prints deploy info.

## Lines 449-456
- Builds backend endpoint and payload for deployment.

## Lines 457-464
- Sends deploy request and parses JSON response.

## Lines 465-472
- Prints agent details, URL, and starts polling loop.

## Lines 473-480
- Polls registry endpoint and extracts agent entry on success.

## Lines 481-488
- Handles active/failed deployment statuses with output and exit.

## Lines 489-496
- Prints deployment timeout warning after polling loop.

## Lines 497-504
- Handles non-200 response errors and raises.

## Lines 505-512
- Handles connection errors, prints URL and tips.

## Lines 513-520
- Handles unexpected deployment exceptions and exits.

## Lines 521-528
- Ends deployment polling with failed/timeout handling.

## Lines 529-536
- Handles non-200 response branch and begins connection-error handler.

## Lines 537-544
- Prints connection error details and handles generic exception.

## Lines 545-552
- Defines local_shell command signature and docstring.

## Lines 553-560
- Ensures docker/compose, prints connect message, starts shell selection.

## Lines 561-568
- Completes shell selection and starts compose exec command list.

## Lines 569-576
- Continues compose exec command arguments.

## Lines 577-584
- Runs compose exec and handles KeyboardInterrupt disconnect.

## Lines 585-592
- Defines local_restart command signature and begins try block.

## Lines 593-600
- Ensures docker/compose, loads env, handles service recreate.

## Lines 601-608
- Runs compose up/restart, prints success, starts exception handling.

## Lines 609-610
- Prints restart error and exits.
