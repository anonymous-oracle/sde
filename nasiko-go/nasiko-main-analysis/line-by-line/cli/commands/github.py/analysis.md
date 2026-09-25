# github.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for time, webbrowser, and typing.

## Lines 9-16
- Imports typer, Console, APIEndpoints, and API client; instantiates console.

## Lines 17-24
- get_github_status fetches token status from backend and handles empty result.

## Lines 25-32
- Prints connected username or disconnected status.

## Lines 33-40
- Returns result or exits on error; starts login_command docstring.

## Lines 41-48
- login_command prints instructions and initializes API client.

## Lines 49-56
- Calls login endpoint to fetch auth URL and handles failure.

## Lines 57-64
- Validates auth URL and prints browser-opening message.

## Lines 65-72
- Attempts to open browser; prints manual URL on failure.

## Lines 73-80
- Handles login initiation error and shows fallback login URL.

## Lines 81-88
- Prints manual URL, sleeps briefly, and prompts user to authorize.

## Lines 89-96
- Sets polling timeout/interval and initializes loop variables.

## Lines 97-104
- Polls token endpoint and checks for successful response.

## Lines 105-112
- Detects connected status, prints success, and breaks loop.

## Lines 113-120
- Prints progress dots and keeps polling on errors.

## Lines 121-128
- Reports timeout and suggests manual status check.

## Lines 129-136
- Exits on timeout and begins logout_command docstring.

## Lines 137-144
- logout_command calls logout endpoint and handles response.

## Lines 145-152
- Prints logout success or failure and exits.

## Lines 153-160
- Handles logout exceptions and starts list_repos_command.

## Lines 161-168
- list_repos_command prints fetching message and begins request.

## Lines 169-176
- Retrieves repositories list and total count from response.

## Lines 177-184
- Handles empty repo list and prints heading for results.

## Lines 185-192
- Iterates repositories and prints name/description.

## Lines 193-200
- Prints privacy/branch info, returns results, or exits on error.

## Lines 201-208
- clone_command docstring describes repo cloning behavior.

## Lines 209-216
- Parses repo argument or selects from list, prints header.

## Lines 217-224
- Handles interactive selection and prints selected repository header.

## Lines 225-232
- Defaults branch to main and prints repo/branch info.

## Lines 233-240
- Initializes client and prints clone/upload status messages.

## Lines 241-248
- Builds clone request and posts to backend, handles response.

## Lines 249-256
- Extracts result data and prints status on success.

## Lines 257-264
- Prints success message and capabilities generation info.

## Lines 265-272
- Reports orchestration trigger status or warning.

## Lines 273-280
- Prints failure, shows validation errors, and exits.

## Lines 281-288
- Handles exceptions during clone/upload.

## Lines 289-296
- _parse_repo_argument docstring and purpose.

## Lines 297-304
- Parses GitHub URL, strips .git suffix, splits owner/repo.

## Lines 305-312
- Returns owner/repo or handles invalid URL and .git trimming.

## Lines 313-320
- Prints format error and examples, then exits.

## Lines 321-328
- _select_repo_from_list docstring and starts repo fetch.

## Lines 329-336
- Fetches repo list, validates response, checks empty list.

## Lines 337-344
- Handles fetch errors and prints selection header.

## Lines 345-352
- Iterates repositories and gathers display fields.

## Lines 353-360
- Prints repo entries with privacy/branch details.

## Lines 361-368
- Prints entries, then starts input selection loop.

## Lines 369-376
- Parses user selection and returns selected repo name.

## Lines 377-383
- Handles invalid input, ValueError, and cancel via KeyboardInterrupt.
