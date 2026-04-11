# router_tests.py — line-by-line analysis

## Lines 1-8
- Imports json/httpx/requests and defines ROUTER_URL with commented token.

## Lines 9-16
- Commented headers block and starts login_and_create_session.

## Lines 17-24
- Builds login payload from superuser credentials with error handling.

## Lines 25-32
- Logs failure, posts login request, and handles response status.

## Lines 33-40
- Parses token from login response and handles request errors.

## Lines 41-48
- Posts create-session request with auth header.

## Lines 49-56
- Extracts session_id and handles request errors.

## Lines 57-64
- Returns session/token and defines test_router with queries list.

## Lines 65-72
- Builds query list and prepares request payload in loop.

## Lines 73-80
- Sends router request with streaming response.

## Lines 81-88
- Prints streaming response messages and handles errors.

## Lines 89-96
- Logs request failure and starts test_router_multiturn.

## Lines 97-104
- Sets multi-turn queries and notes router endpoint.

## Lines 105-112
- Builds first request payload, headers, and initializes route.

## Lines 113-120
- Sends first request and prints response header.

## Lines 121-128
- Parses streamed lines and captures route from final response.

## Lines 129-136
- Logs errors and prepares second request payload.

## Lines 137-144
- Sends second request using captured route.

## Lines 145-152
- Streams second response and handles request errors.

## Lines 153-160
- Ends multi-turn test and starts test_router_with_files.

## Lines 161-168
- Defines file queries, sets router URL, and initializes payload.

## Lines 169-176
- Builds payload/files list with test PDF attachment.

## Lines 177-184
- Sends first file request and streams response.

## Lines 185-192
- Parses response lines, captures route, handles errors.

## Lines 193-200
- Builds payload for second file query.

## Lines 201-208
- Sends second file request and streams response.

## Lines 209-216
- Parses response lines and updates route.

## Lines 217-224
- Handles errors and closes file handle in finally.

## Lines 225-232
- Starts test_router_quality and defines initial compliance queries.

## Lines 233-240
- Adds more compliance-checker query entries.

## Lines 241-248
- Continues compliance-checker queries list.

## Lines 249-256
- Adds compliance queries and begins document-expert queries.

## Lines 257-264
- Adds document-expert queries for summaries.

## Lines 265-272
- Adds audit/report summary and transcript summary queries.

## Lines 273-280
- Adds policy/executive summary queries.

## Lines 281-288
- Adds takeaways and conference summary queries.

## Lines 289-296
- Adds TL;DR and risks queries.

## Lines 297-304
- Adds feedback summary and begins GitHub agent queries.

## Lines 305-312
- Adds GitHub queries for repo summaries/dependencies.

## Lines 313-320
- Adds GitHub queries for docs and structure.

## Lines 321-328
- Adds GitHub queries for PRs and issues.

## Lines 329-336
- Adds GitHub queries for languages and guidelines.

## Lines 337-344
- Adds GitHub queries for repo purpose and tests.

## Lines 345-352
- Adds translator queries for English/German/Japanese.

## Lines 353-360
- Adds translator queries for Spanish and Chinese.

## Lines 361-368
- Adds translator queries for French and Italian.

## Lines 369-376
- Adds translator queries for Russian and Arabic.

## Lines 377-384
- Adds translator queries for German/Spanish to French.

## Lines 385-392
- Closes main queries list; starts commented alternative list.

## Lines 393-400
- Commented-out alternate document-expert queries.

## Lines 401-408
- Commented-out alternate queries continued.

## Lines 409-416
- Commented-out alternate queries continued.

## Lines 417-424
- Commented-out alternate queries continued.

## Lines 425-432
- Commented-out alternate queries continued.

## Lines 433-440
- Commented-out alternate queries and starts another commented block.

## Lines 441-448
- Commented-out queries for document-expert.

## Lines 449-456
- Commented-out queries continued.

## Lines 457-464
- Commented-out queries continued and closes block.

## Lines 465-472
- Iterates queries, builds payload, and sends router request.

## Lines 473-480
- Streams responses and prints agent messages.

## Lines 481-488
- Prints expected agent name for each query.

## Lines 489-496
- Handles request errors and runs tests in __main__ guard.

## Lines 497-497
- Commented-out call for file test.
