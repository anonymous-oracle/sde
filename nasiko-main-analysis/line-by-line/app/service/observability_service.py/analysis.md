# observability_service.py — line-by-line analysis

## Lines 1-8
- Imports FastAPI HTTPException/status, settings, requests/json, typing, and regex helpers.

## Lines 9-16
- Defines ObservabilityService, stores logger, and implements camelCase→snake_case conversion.

## Lines 17-24
- Starts recursive key conversion; handles dicts by mapping keys/values.

## Lines 25-32
- Handles lists and base cases; notes removed Pydantic conversion and starts get_all_sessions.

## Lines 33-40
- get_all_sessions signature/docstring, opens try block, imports AuthClient.

## Lines 41-48
- Initializes AuthClient, fetches accessible agents, and begins empty response for none.

## Lines 49-56
- Completes empty response payload and logs accessible agent count.

## Lines 57-64
- Prepares session collection, iterates agents, and gets project_id per agent.

## Lines 65-72
- Fetches project sessions per agent and aggregates results.

## Lines 73-80
- Increments success count, logs per-agent failures, continues loop.

## Lines 81-88
- Sorts sessions by start_time and starts response payload.

## Lines 89-96
- Completes response payload and enters exception handler.

## Lines 97-104
- Logs error, raises HTTPException, and begins _get_project_sessions_for_aggregation.

## Lines 105-112
- Docstring and time-range selection, defaulting to last 7 days.

## Lines 113-120
- Builds default_start and starts GraphQL query for sessions.

## Lines 121-128
- GraphQL: project node, session edges, and base session fields.

## Lines 129-136
- GraphQL: start/end time, inputs/outputs, and token usage.

## Lines 137-144
- GraphQL: latency quantiles and cost summary totals.

## Lines 145-152
- GraphQL: session annotations with user details.

## Lines 153-160
- GraphQL: annotation summaries with label fractions.

## Lines 161-168
- GraphQL: summary meanScore/name, cursor and pageInfo.

## Lines 169-176
- GraphQL: pagination fields and closes query structure.

## Lines 177-184
- Sets variables, executes query, and extracts project/session edges.

## Lines 185-192
- Iterates sessions, converts to snake_case, and tags with agent_id.

## Lines 193-200
- Logs retrieved count, returns sessions, or logs error on exception.

## Lines 201-208
- Returns empty list on error and starts get_session_details.

## Lines 209-216
- Gets session node id and loads session details for transformation.

## Lines 217-224
- Returns transformed response; handles HTTPException and wraps errors.

## Lines 225-232
- Logs error, raises HTTPException, and starts get_trace_details.

## Lines 233-240
- Builds trace details GraphQL query with project/trace fields.

## Lines 241-248
- GraphQL: root spans and basic span identifiers/status.

## Lines 249-256
- GraphQL: latency and cost summary prompt/completion totals.

## Lines 257-264
- GraphQL: trace id and fragment start for trace tree.

## Lines 265-272
- GraphQL fragment: span list edges and basic span fields.

## Lines 273-280
- GraphQL: span timing, parent, and latency fields.

## Lines 281-288
- GraphQL: token counts and span annotation summaries.

## Lines 289-296
- GraphQL: summary label counts and label fractions.

## Lines 297-304
- GraphQL: summary scores, cursor/node fields, and pageInfo.

## Lines 305-312
- Closes fragment/query, sets variables, and executes request.

## Lines 313-320
- Transforms trace response and handles exceptions.

## Lines 321-328
- Raises HTTPException on errors and starts get_span_details.

## Lines 329-336
- Starts span details GraphQL query and core span identifiers.

## Lines 337-344
- GraphQL: span metadata fields name/kind/status/timing.

## Lines 345-352
- GraphQL: parent/latency/token counts/endTime and input fields.

## Lines 353-360
- GraphQL: output, attributes, and events listing.

## Lines 361-368
- GraphQL: document retrieval metrics fields.

## Lines 369-376
- GraphQL: document evaluation fields.

## Lines 377-384
- GraphQL: span annotations and fragment inclusions.

## Lines 385-392
- Closes span node and starts annotation config fragment.

## Lines 393-400
- GraphQL fragment: annotationConfigs edges with Node id.

## Lines 401-408
- GraphQL: annotation config base name/type/description fields.

## Lines 409-416
- GraphQL: categorical values and continuous bounds/optimization.

## Lines 417-424
- GraphQL: freeform name and closes fragment.

## Lines 425-432
- GraphQL: AnnotationSummaryGroup fragment project configs edges.

## Lines 433-440
- GraphQL: categorical config fields id/name/optimization values.

## Lines 441-448
- GraphQL: categorical values and Node id fields.

## Lines 449-456
- GraphQL: spanAnnotations base fields and timestamps.

## Lines 457-464
- GraphQL: annotator user details.

## Lines 465-472
- GraphQL: spanAnnotationSummaries label fractions.

## Lines 473-480
- GraphQL: summary meanScore/name and start SpanAsideAnnotationList.

## Lines 481-488
- GraphQL: project annotation config edges for aside list.

## Lines 489-496
- GraphQL: config node types and base names.

## Lines 497-504
- GraphQL: spanAnnotations ids and includes summary fragment.

## Lines 505-512
- GraphQL: SpanAside fragment start with project/config node fields.

## Lines 513-520
- GraphQL: annotation config base name/description/type; categorical values start.

## Lines 521-528
- GraphQL: categorical values and continuous bounds.

## Lines 529-536
- GraphQL: freeform names and closes config blocks.

## Lines 537-544
- GraphQL: status code alias, timing, token count, fragment inclusions.

## Lines 545-552
- GraphQL: SpanFeedback fragment start with annotation fields.

## Lines 553-560
- GraphQL: feedback annotation details (label/score/explanation/metadata).

## Lines 561-568
- GraphQL: feedback identifiers, timestamps, and user info.

## Lines 569-576
- GraphQL: SpanHeader fragment base fields.

## Lines 577-584
- GraphQL: SpanHeader timing/token/cost summary.

## Lines 585-592
- GraphQL: TraceHeaderRootSpanAnnotationsFragment and closes query string.

## Lines 593-600
- Sets variables, executes query, transforms span response, handles errors.

## Lines 601-608
- Logs span error and raises HTTPException; starts _get_project_id.

## Lines 609-616
- Builds project URL, sends GET, handles 404 with HTTPException.

## Lines 617-624
- Handles non-200, parses JSON, returns project id.

## Lines 625-632
- Handles request exceptions and raises 502 HTTPException.

## Lines 633-640
- Starts _get_session_node_id and defines GraphQL query.

## Lines 641-648
- Executes query and validates session node presence.

## Lines 649-656
- Raises 404 for missing session and returns node id.

## Lines 657-664
- Starts _get_session_details_by_id and GraphQL query header.

## Lines 665-672
- GraphQL: session metrics, token usage, cost summary totals.

## Lines 673-680
- GraphQL: cost summary prompt/completion, sessionId, latencyP50.

## Lines 681-688
- GraphQL: AnnotationSummaryGroup fragment start with project configs.

## Lines 689-696
- GraphQL: annotation config base/categorical fields.

## Lines 697-704
- GraphQL: categorical values and Node ids.

## Lines 705-712
- GraphQL: spanAnnotations fields and user info.

## Lines 713-720
- GraphQL: user fields and annotation summary start.

## Lines 721-728
- GraphQL: label fraction summaries and mean score/name.

## Lines 729-736
- GraphQL: SessionDetailsTraceList fragment start with traces.

## Lines 737-744
- GraphQL: trace node id/traceId and rootSpan trace cost summary.

## Lines 745-752
- GraphQL: rootSpan id/attributes/project id fields.

## Lines 753-760
- GraphQL: input/output values, token counts, latency, start time.

## Lines 761-768
- GraphQL: spanId, annotation summary, cursor/node.

## Lines 769-776
- GraphQL: pageInfo fields and closes traces block.

## Lines 777-784
- Closes fragment, sets variables including first=100.

## Lines 785-792
- Executes query and starts _execute_graphql_query definition.

## Lines 793-800
- Builds GraphQL URL/payload/headers and opens try.

## Lines 801-808
- Posts request and raises HTTPException on non-200.

## Lines 809-816
- Returns JSON response; handles request exceptions with 502.

## Lines 817-824
- Starts _transform_trace_response, extracts trace data, handles missing.

## Lines 825-832
- Extracts span edges and initializes lookup dictionaries.

## Lines 833-840
- Cleans span data, records spanId/node id in lookups.

## Lines 841-848
- Builds span tree and converts cost/root spans to snake_case.

## Lines 849-856
- Assembles transformed trace response with trace metadata.

## Lines 857-864
- Includes span lookup/project id and returns response.

## Lines 865-872
- Logs transform errors and returns snake_case raw response.

## Lines 873-880
- Starts _clean_span_data and builds normalized span dict.

## Lines 881-888
- Adds timing/parent/latency/token fields and annotation summaries.

## Lines 889-896
- Initializes children list and returns cleaned span.

## Lines 897-904
- Starts _build_span_tree, initializes root_spans and loop.

## Lines 905-912
- Adds root spans or appends to parent children.

## Lines 913-920
- Handles orphan spans with warning logging.

## Lines 921-928
- Defines recursive sorting by start_time.

## Lines 929-936
- Applies recursive sort and returns root_spans; starts _transform_session_response.

## Lines 937-944
- Reads session data and returns empty structure when missing.

## Lines 945-952
- Builds empty session defaults for traces/pagination.

## Lines 953-960
- Starts _transform_session_response, loads session_data, and begins empty response for missing sessions.

## Lines 961-968
- Populates empty session fields: id/session_id/num_traces/token_usage/cost_summary/latency.

## Lines 969-976
- Completes empty response with traces/pagination, then begins trace extraction.

## Lines 977-984
- Initializes traces_edges/cleaned_traces, logs count, and starts edge loop.

## Lines 985-992
- Begins rootSpan cleaning and starts cleaned_root_span dict.

## Lines 993-1000
- Adds core rootSpan fields (spanId, attributes, token counts, latency, startTime, spanAnnotations).

## Lines 1001-1008
- Adds spanAnnotationSummaries and begins project field handling.

## Lines 1009-1016
- Sets project id when present and starts input field conversion.

## Lines 1017-1024
- Builds input mapping and starts output conversion.

## Lines 1025-1032
- Builds output mapping and begins trace field handling.

## Lines 1033-1040
- Builds cleaned_trace_data with costSummary conversion for trace.

## Lines 1041-1048
- Assigns cleaned trace to rootSpan; logs and falls back on clean errors.

## Lines 1049-1056
- Falls back to original rootSpan and starts cleaned_trace dict.

## Lines 1057-1064
- Completes cleaned_trace, appends to list, logs success or empty trace warning.

## Lines 1065-1072
- Logs edge processing errors, reports cleaned count, and begins field conversions.

## Lines 1073-1080
- Converts token_usage, cost_summary, and page_info to snake_case.

## Lines 1081-1088
- Converts traces to snake_case list and prepares response payload.

## Lines 1089-1096
- Returns session response with id/session_id/num_traces/token/cost fields.

## Lines 1097-1104
- Adds latency/traces/pagination and closes response dict.

## Lines 1105-1112
- Handles transform errors and builds fallback response shell.

## Lines 1113-1120
- Fallback session id with guarded access.

## Lines 1121-1128
- Fallback session_id and num_traces fields.

## Lines 1129-1136
- Fallback token_usage and start cost_summary.

## Lines 1137-1144
- Fallback cost_summary and latency_p50 fields.

## Lines 1145-1152
- Fallback traces/pagination and return fallback_response.

## Lines 1153-1160
- Starts get_agent_project_stats and fetches project_id.

## Lines 1161-1168
- Validates project_id and begins project stats GraphQL query.

## Lines 1169-1176
- GraphQL query header for ProjectPageQuery and fragment usage.

## Lines 1177-1184
- Opens ProjectPageHeader_stats fragment and costSummary block.

## Lines 1185-1192
- Defines costSummary prompt/completion fields.

## Lines 1193-1200
- Adds latency quantiles and annotation names, closes fragment.

## Lines 1201-1208
- StreamToggle fragment, closes query, sets variables.

## Lines 1209-1216
- Executes query, extracts project_data, raises 404 if missing.

## Lines 1217-1224
- Converts project data to snake_case and returns payload.

## Lines 1225-1232
- Handles HTTPException/other errors and raises 500.

## Lines 1233-1240
- Starts _transform_span_response, handles missing span_data.

## Lines 1241-1248
- Parses attributes JSON and logs warning on failure.

## Lines 1249-1256
- Starts input JSON parsing when mimeType=json.

## Lines 1257-1264
- Finishes input parsing and starts output JSON parsing.

## Lines 1265-1272
- Parses output JSON and begins snake_case conversion.

## Lines 1273-1280
- Converts span to snake_case, returns payload, and logs exceptions.

## Lines 1281-1281
- Returns snake_case fallback response on transform error.
