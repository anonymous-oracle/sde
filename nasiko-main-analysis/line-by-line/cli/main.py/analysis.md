# main.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports setup/os/sys.

## Lines 9-16
- Imports typer, sets current_dir, and inserts into sys.path.

## Lines 17-24
- Starts _load_env_file_early docstring and search order.

## Lines 25-32
- Continues docstring and imports Path for dotenv loading.

## Lines 33-40
- Defines _load_simple_dotenv and documents supported syntax.

## Lines 41-48
- Reads file text and begins loop over lines.

## Lines 49-56
- Strips comments/exports, checks '=', and splits key/value.

## Lines 57-64
- Validates key and parses empty/quoted values.

## Lines 65-72
- Strips inline comments, honors override, and sets env vars.

## Lines 73-80
- Defines _load_dotenv_file with python-dotenv fallback.

## Lines 81-88
- Scans argv for --config/-c to locate config file.

## Lines 89-96
- Handles --config=, loads explicit config with override.

## Lines 97-104
- Defines search_paths list for env file discovery.

## Lines 105-112
- Iterates search paths and loads first existing env file.

## Lines 113-120
- Creates Typer app and starts version_callback definition.

## Lines 121-128
- Resolves version from metadata with fallback.

## Lines 129-136
- Prints version and defines callback with version option.

## Lines 137-144
- Configures version option and cluster option metadata.

## Lines 145-152
- Sets cluster env var when provided.

## Lines 153-160
- Defines login command and access_key/access_secret options.

## Lines 161-168
- Calls login_standalone and defines logout command.

## Lines 169-176
- Calls logout_command and defines status command.

## Lines 177-184
- Calls status_command and defines whoami command.

## Lines 185-192
- Calls whoami_command and defines docs command.

## Lines 193-200
- Calls api_docs_command and defines list-clusters command.

## Lines 201-208
- Imports list_clusters/Console/Table and prepares cluster list.

## Lines 209-216
- Handles no clusters case and starts building table.

## Lines 217-224
- Adds table columns and iterates cluster rows.

## Lines 225-232
- Adds cluster rows and prints table.

## Lines 233-240
- Adds setup sub-app and starts register_groups definition.

## Lines 241-248
- Imports group apps for github/agent/n8n/chat/search/observability.

## Lines 249-256
- Imports access/user/local/images groups and starts adding typer apps.

## Lines 257-264
- Adds typer apps for each command group.

## Lines 265-272
- Defines main() to load env, register groups, and run app.

## Lines 273-280
- __main__ guard prepares to call main().

## Lines 281-283
- Executes main() when run as a script.
