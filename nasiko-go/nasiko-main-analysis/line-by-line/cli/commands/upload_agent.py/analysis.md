# upload_agent.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports tempfile/zipfile/Path/Optional/typer.

## Lines 9-16
- Imports Console, API endpoints/client, and initializes console.

## Lines 17-24
- Defines upload_zip_command, prints header, and resolves zip path.

## Lines 25-32
- Validates zip exists/is file and checks .zip extension.

## Lines 33-40
- Logs upload path and agent name/auto-detect message.

## Lines 41-48
- Gets API client and builds additional_data with agent name.

## Lines 49-56
- Uploads file via API client and handles response.

## Lines 57-64
- Extracts data, prints status, and success agent name message.

## Lines 65-72
- Prints generated AgentCard/capabilities and orchestration status.

## Lines 73-80
- Handles orchestration warning and starts failure handling.

## Lines 81-88
- Prints validation errors and handles unexpected exceptions.

## Lines 89-96
- Starts upload_directory_command docstring and prints header.

## Lines 97-104
- Validates directory exists/is_dir and logs upload path.

## Lines 105-112
- Logs agent name behavior and begins temp zip creation.

## Lines 113-120
- Creates temp zip file, imports regex, sets version dir pattern.

## Lines 121-128
- Writes directory files to zip, skipping version subdirs.

## Lines 129-136
- Uploads zip file using API client and additional data.

## Lines 137-144
- Handles response, extracts data, and checks success.

## Lines 145-152
- Prints success status and agent name for directory upload.

## Lines 153-160
- Logs generated files and orchestration trigger status.

## Lines 161-168
- Prints upload failure details and validation errors.

## Lines 169-176
- Handles exceptions and starts temp file cleanup.

## Lines 177-184
- Deletes temp zip file or ignores cleanup errors.

## Lines 185-192
- Starts list_user_uploaded_agents_command and prints header.

## Lines 193-200
- Fetches uploaded agents list and handles response.

## Lines 201-208
- Handles no agents case and prints count heading.

## Lines 209-216
- Iterates agents, extracts fields, and reads upload info.

## Lines 217-224
- Chooses status color/icon based on upload status.

## Lines 225-232
- Prints agent name/ID and status line with upload type.

## Lines 233-240
- Prints tags and skills counts when present.

## Lines 241-248
- Prints URL and description for each agent.

## Lines 249-256
- Handles typer exit and begins exception handling.

## Lines 257-264
- Prints unexpected error fetching agents.

## Lines 265-270
- Raises typer.Exit on errors and ends file.
