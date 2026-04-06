# tools.py — line-by-line analysis (part 1)

## Lines 1-8
- Module docstring describes tools for analyzing agent code.
- Imports AST, logging, regex, and Path utilities.

## Lines 9-16
- Imports typing helpers, sets module logger.
- Defines `AgentAnalyzerTools` class and its docstring.

## Lines 17-24
- `glob_files` method signature and docstring start.
- Documents pattern and base_path arguments.

## Lines 25-32
- Describes return structure and logs the glob action.
- Initializes base path and checks existence.

## Lines 33-40
- Handles missing base path with warning and error response dict.

## Lines 41-48
- Builds glob matches list; filters files.
- Logs count and returns success response with files.

## Lines 49-56
- Catches generic exceptions; logs error and returns error response.

## Lines 57-64
- `read_file` method starts with docstring and args.
- Declares return structure and logs read attempt.

## Lines 65-72
- Opens file, reads content, splits into lines.

## Lines 73-80
- Logs line count and returns success dict with content.

## Lines 81-88
- Handles FileNotFoundError with warning and error response.

## Lines 89-96
- Handles other exceptions with error logging and response.

## Lines 97-104
- `grep_code` method signature and docstring start.
- Lists args for pattern, file_path, case sensitivity.

## Lines 105-112
- Describes return value and logs search start.

## Lines 113-120
- Opens file and reads content.
- Sets regex flags and initializes matches; begins line iteration.

## Continuation
- Further line chunks continue in the next update.
