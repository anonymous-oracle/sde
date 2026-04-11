# agent_group.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports Optional/typer, and defines agent_app group.

## Lines 9-16
- Starts upload-zip command and defines zip_file argument.

## Lines 17-24
- Defines optional agent name and upload-zip handler import.

## Lines 25-32
- Calls upload_zip_command and starts upload-directory command.

## Lines 33-40
- Defines upload-directory arguments and optional name options.

## Lines 41-48
- Upload-directory handler call and list-uploaded command start.

## Lines 49-56
- list_uploaded_agents handler call and list command start.

## Lines 57-64
- registry_list options for format/details and docstring.

## Lines 65-72
- registry_list handler call and registry_get command start.

## Lines 73-80
- registry_get arguments, options, and docstring.

## Lines 81-88
- Validates that exactly one search method is provided.

## Lines 89-96
- Errors on missing identifiers and begins identifier selection.

## Lines 97-104
- Determines identifier and search flags for name vs agent_id.

## Lines 105-110
- Imports get_agent_command and executes it.
