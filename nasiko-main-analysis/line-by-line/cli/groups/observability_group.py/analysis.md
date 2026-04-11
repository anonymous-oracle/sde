# observability_group.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports typer, and defines observability_app group.

## Lines 9-16
- Defines sessions command with agent_id/days/limit/format options.

## Lines 17-24
- Delegates sessions command to sessions_command handler.

## Lines 25-32
- Defines session details command with session_id and format option.

## Lines 33-40
- Delegates session_details_command to handler.

## Lines 41-48
- Defines trace command with project/trace ids and format option.

## Lines 49-56
- Delegates trace_details_command to handler.

## Lines 57-64
- Defines span command with span_id and format option.

## Lines 65-72
- Delegates span_details_command to handler.

## Lines 73-82
- Defines stats command and delegates agent_stats_command.
