# access_group.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports List/typer, and defines access_app group.

## Lines 9-16
- Registers grant-user command with agent_id and user_ids options.

## Lines 17-24
- Calls grant_user_access_command and starts grant-agent command.

## Lines 25-32
- Defines grant-agent args with target_agent_ids option.

## Lines 33-40
- Calls grant_agent_access_command and starts list command.

## Lines 41-48
- list command invokes list_agent_access_command.

## Lines 49-56
- Registers revoke-user command with user_ids.

## Lines 57-64
- Calls revoke_user_access_command and starts revoke-agent command.

## Lines 65-72
- Defines revoke-agent args and help text.

## Lines 73-78
- Calls revoke_agent_access_command.
