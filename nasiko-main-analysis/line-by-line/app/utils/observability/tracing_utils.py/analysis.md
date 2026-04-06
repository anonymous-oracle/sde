# tracing_utils.py — line-by-line analysis

## Lines 1-8
- Imports OS, JSON, logging, importlib, ContextVar, Optional.
- Imports OpenTelemetry trace API and SpanProcessor classes.

## Lines 9-16
- Imports OTLP exporter and Phoenix register function.
- Initializes logger and session_id context var.

## Lines 17-24
- Defines `bootstrap_tracing` signature and docstring header.

## Lines 25-32
- Docstring explains args: project_name, endpoint, instrumentors, framework.

## Lines 33-40
- Reads collector endpoint from env if not provided.
- Checks TRACING_ENABLED and returns if disabled.

## Lines 41-48
- Chooses instrumentors based on framework when not provided.
- Logs bootstrap start.

## Lines 49-56
- Registers Phoenix tracing provider and adds session id processor.
- Adds OTLP span processor targeting endpoint.

## Lines 57-64
- Iterates instrumentors and applies `.instrument` when available.
- Logs warning on instrumentor failures.

## Lines 65-72
- Applies uvicorn patch hook and logs success.

## Lines 73-80
- Logs failure to initialize tracing on exception.
- Begins `_get_instrumentors_for_framework`.

## Lines 81-88
- Docstring for framework instrumentor selection.
- Defines nested try_import_instrumentor helper.

## Lines 89-96
- try_import_instrumentor imports module/class and logs warnings on failure.
- Returns None if unavailable.

## Lines 97-104
- Defines framework_instrumentors mapping for LangChain and CrewAI.

## Lines 105-112
- Adds mappings for AutoGen and LlamaIndex.

## Lines 113-120
- Adds DSPy and Haystack mappings.

## Lines 121-128
- Adds anthropic, pydantic-ai, minimax, custom mappings.

## Lines 129-136
- Chooses framework-specific instrumentors or default LangChain+OpenAI.

## Lines 137-144
- Iterates specs and imports instrumentor classes into list.

## Lines 145-152
- Falls back to OpenAI instrumentor if none found.

## Lines 153-160
- Logs selected instrumentors and returns list.
- Starts internals section.

## Lines 161-168
- Defines ContextSessionIdProcessor class.
- on_start sets span attribute from context var.

## Lines 169-176
- Defines on_end/shutdown/force_flush as no-ops.

## Lines 177-184
- Starts _patch_uvicorn; imports uvicorn and checks if already patched.

## Lines 185-192
- Saves original run and defines patched_run.
- Adds middleware if app supports it.

## Lines 193-200
- Marks patched flag and swaps uvicorn.run.
- Ignores ImportError.

## Lines 201-208
- Starts optional BaseHTTPMiddleware import block.
- Defines _JsonRpcSessionMiddleware class.

## Lines 209-216
- Reads request body and parses JSON.
- Extracts session id and sets span attribute.

## Lines 217-224
- Defines custom receive to reuse body; assigns to request._receive.
- Ignores parse errors.

## Lines 225-232
- Calls next middleware/handler and resets context var afterward.

## Lines 233-236
- On ImportError, disables middleware by setting None.
