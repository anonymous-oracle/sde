# chat_group.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports Optional/typer, defines chat_app group.

## Lines 9-16
- Defines create-session command with optional agent name.

## Lines 17-24
- Delegates create_session and starts list-sessions command.

## Lines 25-32
- Defines list-sessions options for limit/cursor/direction.

## Lines 33-40
- Delegates list_sessions and starts history command.

## Lines 41-48
- Defines history command with session_id/limit/cursor/direction.

## Lines 49-56
- Delegates get_chat_history and starts delete-session command.

## Lines 57-64
- Defines delete-session command and delegates to handler.

## Lines 65-72
- Defines send command with url/session/message options.

## Lines 73-80
- Continues send options and prompt settings.

## Lines 81-88
- send command docstring and handler import.

## Lines 89-90
- Calls send_message_command.
