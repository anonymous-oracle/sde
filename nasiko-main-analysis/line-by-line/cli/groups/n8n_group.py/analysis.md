# n8n_group.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports Optional/typer, defines n8n_app group.

## Lines 9-16
- Defines register command with workflow_id/name/description options.

## Lines 17-24
- Delegates register_workflow and defines connect command args.

## Lines 25-32
- Defines connect options for URL/API key/connection name.

## Lines 33-40
- Delegates connect_n8n and defines credentials command.

## Lines 41-48
- Delegates get_n8n_credentials and defines update command args.

## Lines 49-56
- Defines update options and delegates update_n8n_credentials.

## Lines 57-64
- Defines delete command and delegates delete_n8n_credentials.

## Lines 65-72
- Defines workflows command with active_only/limit options.

## Lines 73-80
- Delegates list_n8n_workflows to handler.

## Lines 81-95
- Ends workflows command and file.
