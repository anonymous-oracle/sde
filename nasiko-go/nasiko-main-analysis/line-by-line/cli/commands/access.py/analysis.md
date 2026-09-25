# access.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports typer/List/Rich console helper.

## Lines 9-16
- Imports API client, initializes console, and starts grant_user_access_command.

## Lines 17-24
- Prints header/agent/user info and starts API call try block.

## Lines 25-32
- Builds request payload and posts to user access endpoint.

## Lines 33-40
- Handles response, prints success message and granted count.

## Lines 41-48
- Iterates granted users list and prints each user id.

## Lines 49-56
- Handles failure response and raises Exit on error.

## Lines 57-64
- Handles exceptions and starts grant_agent_access_command.

## Lines 65-72
- Prints header/agent info and begins API call for agent access.

## Lines 73-80
- Builds payload and posts to agent access endpoint.

## Lines 81-88
- Handles response, prints success message and granted count.

## Lines 89-96
- Iterates granted agents list and prints each agent id.

## Lines 97-104
- Handles failure response and raises Exit on error.

## Lines 105-112
- Handles exceptions and starts list_agent_access_command.

## Lines 113-120
- Prints header/agent info and begins fetch access info.

## Lines 121-128
- Calls permissions endpoint and validates response.

## Lines 129-136
- Prints owner ID and begins users list output.

## Lines 137-144
- Prints users with access or no-users message.

## Lines 145-152
- Prints agents with access or no-agents message.

## Lines 153-160
- Handles exceptions and starts revoke_user_access_command.

## Lines 161-168
- Prints header/agent/user info and begins revoke process.

## Lines 169-176
- Prepares revoke lists and loops over user ids.

## Lines 177-184
- Sends delete request per user and handles success/failure.

## Lines 185-192
- Handles per-user exception and records failure.

## Lines 193-200
- Prints revoked users summary and list.

## Lines 201-208
- Prints failed users summary and optionally exits.

## Lines 209-216
- Handles exceptions and starts revoke_agent_access_command.

## Lines 217-224
- Prints header/agent info and begins agent revoke loop.

## Lines 225-232
- Sends delete request per agent and handles success/failure.

## Lines 233-240
- Handles per-agent exceptions and records failure.

## Lines 241-248
- Prints revoked agents summary and list.

## Lines 249-256
- Prints failed agents summary and optionally exits.

## Lines 257-264
- Handles exceptions and starts revoke_agent_access_command end.

## Lines 265-272
- Continues error handling and raises Exit on failures.

## Lines 273-280
- End of revoke_agent_access_command error handling.

## Lines 281-288
- File end (no additional commands defined).

## Lines 289-296
- End of file.

## Lines 297-299
- End of file.
