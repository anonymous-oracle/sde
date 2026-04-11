# config.py — line-by-line analysis

## Lines 1-8
- Imports os and typing List.
- Defines ObservabilityConfig class with docstring.

## Lines 9-16
- get_phoenix_endpoint reads env or default Phoenix collector URL.

## Lines 17-24
- is_tracing_enabled checks TRACING_ENABLED flag.
- get_project_prefix reads TRACING_PROJECT_PREFIX.

## Lines 25-32
- get_required_dependencies returns list of tracing packages.
- Includes Phoenix, OpenInference, OTEL SDK/exporter, pytz.

## Lines 33-40
- get_injection_enabled checks OBSERVABILITY_INJECTION_ENABLED flag.

## Lines 41-47
- get_log_level reads OBSERVABILITY_LOG_LEVEL with default INFO.
