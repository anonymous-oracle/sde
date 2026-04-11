# registry.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for datetime, requests, and Console.

## Lines 9-16
- Imports Rich JSON/Panel/Table, sys/os, and appends CLI path.

## Lines 17-24
- Imports API endpoints and client; defines list_agents_command.

## Lines 25-32
- Calls registry endpoint and handles response with success message.

## Lines 33-40
- Validates data, extracts agents list, and handles empty registry.

## Lines 41-48
- Prints header and dispatches to table/json/list display.

## Lines 49-56
- Handles connection errors and timeouts for list call.

## Lines 57-64
- Handles HTTP errors and generic exceptions.

## Lines 65-72
- Defines get_agent_command parameters and docstring.

## Lines 73-80
- Fetches by agent ID endpoint and tracks identifier type.

## Lines 81-88
- Fetches by name endpoint and handles 404 not found.

## Lines 89-96
- Raises for status, parses JSON, and chooses display format.

## Lines 97-104
- Displays JSON/details and handles connection errors.

## Lines 105-112
- Handles timeout/HTTP errors for get_agent_command.

## Lines 113-120
- Prints generic error and starts display_agent_details.

## Lines 121-128
- Chooses data payload and builds basic info string.

## Lines 129-136
- Adds protocol/description/url/transport and prints basic panel.

## Lines 137-144
- Builds provider panel and starts resources info.

## Lines 145-152
- Adds icon/documentation URLs and prints resources panel.

## Lines 153-160
- Builds capabilities info from dict and prints panel.

## Lines 161-168
- Prepares input/output modes section and prints panel.

## Lines 169-176
- Adds input/output modes to info and prints when present.

## Lines 177-184
- Builds security info from schemes and security entries.

## Lines 185-192
- Prints security panel and starts skills listing.

## Lines 193-200
- Iterates skills and builds initial skill info fields.

## Lines 201-208
- Appends tags/examples to skill info text.

## Lines 209-216
- Appends input/output modes for each skill entry.

## Lines 217-224
- Prints skill panel with name and ordering.

## Lines 225-232
- Collects additional fields including supportsAuthenticatedExtendedCard.

## Lines 233-240
- Adds signatures/additionalInterfaces and parses created_at.

## Lines 241-248
- Parses updated_at and prints additional info panel.

## Lines 249-256
- Ends additional info panel rendering.

## Lines 257-264
- Starts display_agent_capabilities and normalizes data payload.

## Lines 265-272
- Extracts agent name/skills and handles missing skills.

## Lines 273-280
- Prints skills header and begins per-skill info formatting.

## Lines 281-288
- Adds tags/examples and formats example list.

## Lines 289-296
- Prints skill panel and spacing between entries.

## Lines 297-304
- Defines display_agents_table and sets table styling.

## Lines 305-312
- Adds columns and optional description column.

## Lines 313-320
- Builds row data from agent fields and tags.

## Lines 321-328
- Adds description when requested, prints table.

## Lines 329-336
- Defines JSON and list display helpers.

## Lines 337-344
- Iterates agents to build list display and counts skills.

## Lines 345-352
- Builds list display string with ID/URL/version/skills.

## Lines 353-360
- Prints list entry and spacing between agents.

## Lines 361-368
- Defines api_docs_command for docs and Swagger links.

## Lines 369-376
- Builds docs/redoc/openapi URLs and checks server health.

## Lines 377-384
- Starts docs_info string with docs endpoints header.

## Lines 385-392
- Adds Swagger/Redoc and key endpoint list entries.

## Lines 393-400
- Continues endpoint list and usage guidance.

## Lines 401-408
- Completes usage guidance and documentation text.

## Lines 409-416
- Prints docs panel and success messages.

## Lines 417-424
- Handles connection errors/timeouts and prints expected URL.

## Lines 425-432
- Handles other exceptions and prepares fallback docs URL.

## Lines 433-437
- Prints fallback docs URL when server is down.
