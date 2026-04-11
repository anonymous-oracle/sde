# search.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports typer/Rich, and pulls API endpoints/client.

## Lines 9-16
- Creates Console and starts search_users definition with docstring.

## Lines 17-24
- Validates query length, gets API client, and builds params.

## Lines 25-32
- Calls search endpoint, handles response, and initializes user list.

## Lines 33-40
- Extracts totals and prints heading for user results.

## Lines 41-48
- Builds Rich table columns and starts iterating user rows.

## Lines 49-56
- Adds user rows and prints the table.

## Lines 57-64
- Prints no-users message and handles exceptions with error output.

## Lines 65-72
- Starts search_agents definition and validates query length.

## Lines 73-80
- Gets API client, builds params, and calls search endpoint.

## Lines 81-88
- Parses response, totals, and prints agent results heading.

## Lines 89-96
- Creates table columns for agent name/id/description/tags.

## Lines 97-104
- Extracts agent fields and prepares tag string formatting.

## Lines 105-112
- Continues tag formatting and adds agent row to table.

## Lines 113-120
- Prints table or no-agents message.

## Lines 121-128
- Handles typer exit and generic exception reporting.
