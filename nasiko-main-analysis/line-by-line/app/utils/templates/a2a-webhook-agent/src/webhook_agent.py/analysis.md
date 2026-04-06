# webhook_agent.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for json, logging, httpx.
- Initializes module logger.

## Lines 9-16
- Defines WebhookAgent class with docstring.
- __init__ signature begins.

## Lines 17-24
- Stores webhook_url/timeout and logs init.
- Starts send_message method with docstring.

## Lines 25-32
- Documents args and return type for send_message.

## Lines 33-40
- Prepares webhook payload and logs URL/payload.
- Starts HTTP call block.

## Lines 41-48
- Uses httpx AsyncClient to POST JSON payload.
- Raises on non-2xx and passes response to processing.

## Lines 49-56
- Returns processed webhook response.
- Handles timeout with logged exception.

## Lines 57-64
- Handles HTTP status errors with message and raise.
- Handles generic exceptions similarly.

## Lines 65-72
- Starts _process_webhook_response with docstring.
- Reads response text and checks for streamed format.

## Lines 73-80
- If streamed, accumulates content; else attempts JSON parse.

## Lines 81-88
- Logs JSON response and searches for known response fields.

## Lines 89-96
- Iterates preferred fields; returns first match as text.
- Logs extracted field.

## Lines 97-104
- If no field, returns formatted JSON; else returns str of data.

## Lines 105-112
- Handles JSON decode errors; returns raw text.

## Lines 113-120
- Starts _is_streamed_response and splits lines.
- Returns False if only one line.

## Lines 121-128
- Counts JSON lines with "type" field.
- Returns True if at least two match.

## Lines 129-136
- Starts _accumulate_streamed_content with expected format.
- Initializes accumulator and logs line count.

## Lines 137-144
- Iterates lines; skips empty; parses JSON per line.

## Lines 145-152
- Accumulates content from items of type "item".
- Logs failures for invalid JSON lines.

## Lines 153-160
- Logs accumulated content and returns it or default message.

## Lines 161-168
- Parses each streamed line as JSON.
- Checks for item-type messages with content.

## Lines 169-176
- Appends item content; logs JSON parsing failures.
- Continues loop on errors.

## Lines 177-184
- Logs accumulated content and returns it or fallback text.
- Ends streamed response helper.

## Lines 185-192
- Defines create_agent and docstring; imports os.
- Reads WEBHOOK_URL and WEBHOOK_TIMEOUT from env.

## Lines 193-200
- Raises if WEBHOOK_URL missing; creates WebhookAgent.
- Starts return dict with name/description.

## Lines 201-205
- Adds version and webhook_agent instance; closes return dict.
