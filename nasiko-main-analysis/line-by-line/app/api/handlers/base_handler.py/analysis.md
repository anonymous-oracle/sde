# base_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring, typing import, and BaseHandler class declaration begins.

## Lines 9-16
- Class docstring plus __init__ storing service and logger.

## Lines 17-24
- log_info helper formats kwargs when present and writes info logs.

## Lines 25-32
- log_error formats error details; log_warning method begins.

## Lines 33-40
- log_warning logs with optional kwargs; log_debug method signature and docstring.

## Lines 41-48
- log_debug logs with optional kwargs; handle_service_error logs and prepares to raise.

## Lines 49-56
- handle_service_error raises; validate_required_fields signature and missing_fields comprehension starts.

## Lines 57-64
- missing_fields detection and logging; returns False when missing, True otherwise.

## Lines 65-72
- sanitize_string trims/limits strings; build_success_response signature.

## Lines 73-80
- build_success_response returns standardized payload; build_error_response signature/docstring.

## Lines 81-85
- build_error_response constructs error payload with optional error_code.
