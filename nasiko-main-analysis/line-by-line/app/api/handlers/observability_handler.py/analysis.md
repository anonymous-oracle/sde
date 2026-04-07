# observability_handler.py — line-by-line analysis

## Lines 1-8
- Imports and ObservabilityHandler class declaration with __init__ signature.

## Lines 9-16
- __init__ stores service/logger and creates ObservabilityService; get_session_details delegates to service.

## Lines 17-24
- get_trace_details and get_span_details delegate to ObservabilityService.

## Lines 25-32
- get_all_sessions passes user_id/auth_header/start_time to service for multi-agent session retrieval.

## Lines 33-39
- get_agent_project_stats delegates to service for agent-specific stats.
