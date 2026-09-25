# observability.py — line-by-line analysis

## Lines 1-8
- Imports modules and CLI dependencies.

## Lines 9-16
- Imports modules and CLI dependencies.

## Lines 17-24
- Defines function(s) format_datetime with loops, conditionals, returns.

## Lines 25-32
- Defines configuration or data variables: dt.

## Lines 33-40
- Defines function(s) format_duration with conditionals, error handling, returns.

## Lines 41-48
- Defines configuration or data variables: duration_ms.

## Lines 49-56
- Defines function(s) format_cost with loops, error handling, returns.

## Lines 57-64
- Defines configuration or data variables: cost_val.

## Lines 65-72
- Defines function(s) format_tokens with loops, conditionals, error handling, returns.

## Lines 73-80
- Defines configuration or data variables: tokens_val.

## Lines 81-88
- Defines function(s) get_status_color with loops.

## Lines 89-96
- Continues CLI logic and output handling.

## Lines 97-104
- Defines function(s) get_auth_headers with conditionals, returns.

## Lines 105-112
- Defines function(s) sessions_command with returns.

## Lines 113-120
- Continues CLI logic and output handling.

## Lines 121-128
- Loop logic for processing results or output.

## Lines 129-136
- Defines configuration or data variables: headers, start_time, params.

## Lines 137-144
- Defines configuration or data variables: console, task, response.

## Lines 145-152
- Defines configuration or data variables: params, timeout.

## Lines 153-160
- Defines configuration or data variables: data.

## Lines 161-168
- Defines configuration or data variables: sessions_data, sessions.

## Lines 169-176
- Defines configuration or data variables: sessions.

## Lines 177-184
- Defines configuration or data variables: sessions, total_agents, successful_agents.

## Lines 185-192
- Defines configuration or data variables: header_text, stats_text.

## Lines 193-200
- Conditional logic for CLI branching.

## Lines 201-208
- Continues CLI logic and output handling.

## Lines 209-216
- Conditional logic for CLI branching.

## Lines 217-224
- Defines function(s) session_details_command.

## Lines 225-232
- Defines configuration or data variables: headers, url.

## Lines 233-240
- Defines configuration or data variables: console, task, response.

## Lines 241-248
- Defines configuration or data variables: data.

## Lines 249-256
- Defines configuration or data variables: session.

## Lines 257-264
- Conditional logic for CLI branching.

## Lines 265-272
- Continues CLI logic and output handling.

## Lines 273-280
- Defines function(s) trace_details_command with error handling.

## Lines 281-288
- Continues CLI logic and output handling.

## Lines 289-296
- Defines configuration or data variables: headers, url, project_id.

## Lines 297-304
- Defines configuration or data variables: console, task, response.

## Lines 305-312
- Defines configuration or data variables: data.

## Lines 313-320
- Defines configuration or data variables: trace.

## Lines 321-328
- Conditional logic for CLI branching.

## Lines 329-336
- Continues CLI logic and output handling.

## Lines 337-344
- Defines function(s) span_details_command with error handling.

## Lines 345-352
- Defines configuration or data variables: headers.

## Lines 353-360
- Defines configuration or data variables: url, console, task.

## Lines 361-368
- Defines configuration or data variables: response.

## Lines 369-376
- Defines configuration or data variables: data, span.

## Lines 377-384
- Conditional logic for CLI branching.

## Lines 385-392
- Continues CLI logic and output handling.

## Lines 393-400
- Defines function(s) agent_stats_command with error handling.

## Lines 401-408
- Loop logic for processing results or output.

## Lines 409-416
- Defines configuration or data variables: headers, start_time, url.

## Lines 417-424
- Defines configuration or data variables: console, task, response.

## Lines 425-432
- Defines configuration or data variables: data.

## Lines 433-440
- Defines configuration or data variables: project_stats.

## Lines 441-448
- Continues CLI logic and output handling.

## Lines 449-456
- Continues CLI logic and output handling.

## Lines 457-464
- Defines function(s) display_sessions_table.

## Lines 465-472
- Loop logic for processing results or output.

## Lines 473-480
- Defines configuration or data variables: agent_id, session_id, num_traces.

## Lines 481-488
- Defines configuration or data variables: token_usage, total_tokens, cost_summary.

## Lines 489-496
- Defines configuration or data variables: latency, start_time.

## Lines 497-504
- Continues CLI logic and output handling.

## Lines 505-512
- Defines function(s) display_sessions_summary.

## Lines 513-520
- Defines configuration or data variables: total_traces, total_tokens, total_cost.

## Lines 521-528
- Defines configuration or data variables: agents, agent_id.

## Lines 529-536
- Defines configuration or data variables: metrics_info.

## Lines 537-544
- Defines configuration or data variables: agent_info, sorted_agents, percentage.

## Lines 545-552
- Defines function(s) display_session_details.

## Lines 553-560
- Defines configuration or data variables: session_id, overview_info.

## Lines 561-568
- Defines configuration or data variables: token_usage.

## Lines 569-576
- Defines configuration or data variables: cost_summary, total_cost, prompt_cost.

## Lines 577-584
- Defines configuration or data variables: traces.

## Lines 585-592
- Defines function(s) display_session_traces with conditionals.

## Lines 593-600
- Defines configuration or data variables: session_id.

## Lines 601-608
- Defines function(s) display_traces_table.

## Lines 609-616
- Defines configuration or data variables: root_span, project_data, project_id.

## Lines 617-624
- Defines configuration or data variables: trace_id, root_span, tokens.

## Lines 625-632
- Defines configuration or data variables: start_time, trace_data, cost_summary.

## Lines 633-640
- Defines function(s) fetch_session_history with loops, error handling.

## Lines 641-648
- Defines configuration or data variables: url, response, data.

## Lines 649-656
- Returns values from helper logic.

## Lines 657-664
- Defines function(s) get_enhanced_trace_io with loops, conditionals.

## Lines 665-672
- Defines configuration or data variables: hist_input, hist_output, root_span.

## Lines 673-680
- Defines configuration or data variables: input_obj, output_obj, hist_input.

## Lines 681-688
- Defines configuration or data variables: input_display, output_display, root_span.

## Lines 689-696
- Defines configuration or data variables: fallback_output, input_obj, output_obj.

## Lines 697-704
- Defines function(s) format_io_for_table with returns.

## Lines 705-712
- Defines configuration or data variables: cleaned.

## Lines 713-720
- Defines function(s) display_trace_tree with conditionals, returns.

## Lines 721-728
- Defines configuration or data variables: trace_info.

## Lines 729-736
- Defines configuration or data variables: cost_summary, total_cost.

## Lines 737-744
- Defines function(s) display_spans_recursive with conditionals.

## Lines 745-752
- Defines configuration or data variables: indent, status_color, span_id.

## Lines 753-760
- Defines configuration or data variables: span_db_id, span_id_short, span_db_id_short.

## Lines 761-768
- Defines configuration or data variables: id_display, span_info.

## Lines 769-776
- Conditional logic for CLI branching.

## Lines 777-784
- Defines function(s) display_trace_spans_flat with conditionals.

## Lines 785-792
- Defines function(s) flatten_spans with loops, conditionals.

## Lines 793-800
- Defines configuration or data variables: all_spans.

## Lines 801-808
- Defines configuration or data variables: table.

## Lines 809-816
- Defines configuration or data variables: span_id.

## Lines 817-824
- Defines configuration or data variables: name, kind, status.

## Lines 825-832
- Defines configuration or data variables: colored_status, latency, tokens.

## Lines 833-840
- Defines function(s) display_span_details.

## Lines 841-848
- Defines configuration or data variables: span_name, span_kind, status_code.

## Lines 849-856
- Conditional logic for CLI branching.

## Lines 857-864
- Defines configuration or data variables: parent_id.

## Lines 865-872
- Imports modules and CLI dependencies.

## Lines 873-880
- Defines configuration or data variables: attributes_data.

## Lines 881-888
- Defines configuration or data variables: input_data, output_data, io_info.

## Lines 889-896
- Defines configuration or data variables: input_text.

## Lines 897-904
- Defines configuration or data variables: output_text.

## Lines 905-912
- Defines configuration or data variables: annotations.

## Lines 913-920
- Defines configuration or data variables: annotation_name, annotation_value.

## Lines 921-928
- Defines function(s) display_agent_stats.

## Lines 929-936
- Defines configuration or data variables: trace_count, latency_p50, latency_p99.

## Lines 937-944
- Defines configuration or data variables: cost_summary, total_cost, prompt_cost.

## Lines 945-952
- Defines configuration or data variables: cost_info.

## Lines 953-960
- Defines configuration or data variables: annotation_names, annotations_text.

## Lines 961-968
- Defines configuration or data variables: doc_eval_names, eval_text.

## Lines 969-974
- Conditional logic for CLI branching.
