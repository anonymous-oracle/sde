# instrumentation_injector.py — line-by-line analysis

## Lines 1-8
- Module docstring and logging/os imports.

## Lines 9-16
- Creates logger, defines InstrumentationInjector, and loads template in __init__.

## Lines 17-24
- Starts inject_langtrace_config, checks LANGTRACE_ENABLED, lists main.py candidates.

## Lines 25-32
- Adds remaining candidate paths and initializes main/config variables.

## Lines 33-40
- Searches for main.py and prepares missing-file guard.

## Lines 41-48
- Logs missing main.py, writes langtrace_config.py template file.

## Lines 49-56
- Logs creation, reads main.py, checks for existing import.

## Lines 57-64
- Skips injection if import exists; splits lines and initializes insertion state.

## Lines 65-72
- Iterates lines, skips shebangs and encoding declarations.

## Lines 73-80
- Continues encoding skip and begins docstring handling.

## Lines 81-88
- Handles single-line docstrings and sets insertion index.

## Lines 89-96
- Handles multi-line docstrings and moves insertion index.

## Lines 97-104
- Detects import/from/__future__ lines and marks imports found.

## Lines 105-112
- Detects multi-line imports and searches for their end.

## Lines 113-120
- Tracks end of multiline imports or backslash continuations.

## Lines 121-128
- Handles single-line imports and updates insert position.

## Lines 129-136
- Skips comments/blank lines after imports to place injection.

## Lines 137-144
- Inserts langtrace_config import before first code line.

## Lines 145-152
- Writes modified main.py, logs injection position, returns True.

## Lines 153-160
- Starts _get_langtrace_config_template and template imports/env vars.

## Lines 161-168
- Prints masked API key/host and starts Langtrace init try block.

## Lines 169-176
- Initializes langtrace and begins instrumentation list.

## Lines 177-184
- Adds LangChain/OpenAI and LLM library instrumentations.

## Lines 185-192
- Adds CrewAI and web framework instrumentation entries.

## Lines 193-200
- Adds HTTP client instrumentations and starts DB entries.

## Lines 201-208
- Adds DB/vector DB instrumentations and closes list.

## Lines 209-216
- Iterates instrumentations, imports modules, and instruments them.

## Lines 217-224
- Counts instrumentations and logs failures/summary.

## Lines 225-232
- Begins OpenTelemetry session context injection imports and helpers.

## Lines 233-240
- Defines SessionContextSpanProcessor and stores agent name.

## Lines 241-248
- on_start reads session context and sets span attributes.

## Lines 249-256
- Logs injection errors and defines on_end stub.

## Lines 257-264
- Defines shutdown/force_flush stubs.

## Lines 265-272
- Adds span processor to tracer provider or warns.

## Lines 273-280
- Starts OTLPSpanExporter monkey patch setup and stores originals.

## Lines 281-288
- patched_export iterates spans and skips when session already set.

## Lines 289-296
- Extracts session_id from langchain.metadata JSON.

## Lines 297-304
- Reads nested metadata/session_id and falls back to inputs.

## Lines 305-312
- Parses langchain.inputs for metadata/configurable session_id.

## Lines 313-320
- Handles parsing errors and injects session attributes when found.

## Lines 321-328
- Updates span attributes with session and agent info.

## Lines 329-336
- Calls original exporter or falls back on errors.

## Lines 337-344
- Applies monkey patch and handles exporter import failures.

## Lines 345-352
- Imports FastAPI middleware base and declares middleware class.

## Lines 353-360
- Starts dispatch handler and sets up session_id extraction flow.

## Lines 361-368
- Checks path/query params and begins JSON-RPC parsing.

## Lines 369-376
- Parses JSON body for JSON-RPC and validates params structure.

## Lines 377-384
- Extracts sessionId from metadata and restores request body.

## Lines 385-392
- Handles JSON parsing errors and multipart form detection.

## Lines 393-400
- Parses urlencoded form data for session_id and restores body.

## Lines 401-408
- Handles form errors and prepares context attach.

## Lines 409-416
- Attaches context, calls next handler, and detaches.

## Lines 417-424
- Continues without session_id or handles middleware exceptions.

## Lines 425-432
- Begins monkey patch section and captures FastAPI __init__.

## Lines 433-440
- Defines patched_fastapi_init and adds middleware with errors.

## Lines 441-448
- Assigns patched FastAPI init and starts Starlette patch block.

## Lines 449-456
- Defines patched_starlette_init and adds middleware.

## Lines 457-464
- Assigns Starlette init and logs success or failures.

## Lines 465-472
- Handles missing Starlette and logs FastAPI-only setup.

## Lines 473-480
- Handles no-session branch and middleware exceptions by continuing request.

## Lines 481-488
- Ends middleware exception handling and starts FastAPI monkey patch setup.

## Lines 489-496
- Calls original FastAPI init, adds middleware, logs failures.

## Lines 497-504
- Assigns patched FastAPI init and starts Starlette patch/imports.

## Lines 505-512
- Defines patched Starlette init and adds middleware with error handling.

## Lines 513-520
- Assigns patched Starlette init and handles missing Starlette fallback.

## Lines 521-528
- Handles OpenTelemetry setup failures and outer Langtrace exception.

## Lines 529-532
- Logs missing API key branch and closes template string.
