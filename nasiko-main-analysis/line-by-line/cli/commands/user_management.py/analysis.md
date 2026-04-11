# user_management.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports typer, Console, and API client.

## Lines 9-16
- Initializes console and begins register_user_command definition.

## Lines 17-24
- Prints registration header, shows inputs, and starts try block.

## Lines 25-32
- Builds request payload and prints registering message.

## Lines 33-40
- Sends register request, handles response, and prints success/user ID.

## Lines 41-48
- Prints role/status and starts credentials warning section.

## Lines 49-56
- Prints access key/secret warning and handles exceptions.

## Lines 57-64
- Handles errors and starts list_users_command definition.

## Lines 65-72
- Prints list header, gets client, and announces fetch.

## Lines 73-80
- Calls auth_get, validates response, and handles no users.

## Lines 81-88
- Prints count and iterates users, extracting fields.

## Lines 89-96
- Formats role/status and prints user summary line.

## Lines 97-104
- Prints created/last login and handles exceptions.

## Lines 105-112
- Handles errors and starts get_user_command definition.

## Lines 113-120
- Prints detail header, fetches user, and handles response.

## Lines 121-128
- Prints "User found" and extracts user attributes.

## Lines 129-136
- Reads role/status/created/last login/created_by fields.

## Lines 137-144
- Builds role/status and prints username/email and status lines.

## Lines 145-152
- Prints created/last login/created by and handles exceptions.

## Lines 153-160
- Handles errors and starts regenerate_credentials_command.

## Lines 161-168
- Prints header, gets client, and posts regenerate request.

## Lines 169-176
- Handles response and prints regeneration success message.

## Lines 177-184
- Prints new access key/secret and warning.

## Lines 185-192
- Handles errors and starts revoke_user_command definition.

## Lines 193-200
- Prints revoke header, gets client, and posts revoke tokens.

## Lines 201-208
- Handles response, prints revoked count or errors.

## Lines 209-216
- Handles errors and starts reinstate_user_command definition.

## Lines 217-224
- Prints reinstate header, gets client, and posts reinstate.

## Lines 225-232
- Handles response and prints success with user ID.

## Lines 233-240
- Prints username/email/role/status/created_on details.

## Lines 241-248
- Prints new credentials header and access key/secret lines.

## Lines 249-256
- Prints warning and handles reinstate errors.

## Lines 257-264
- Starts delete_user_command with header and confirmation notice.

## Lines 265-272
- Prompts confirmation and cancels when declined.

## Lines 273-280
- Starts delete try block, gets client, and sends delete request.

## Lines 281-288
- Handles delete response and checks for success.

## Lines 289-296
- Prints delete success or failure and raises on error.

## Lines 297-304
- Handles typer exit and generic delete errors.

## Lines 305-312
- Continues delete error handling and exits on failure.

## Lines 313-320
- Final delete exception logging and raises Exit.

## Lines 321-327
- Ends delete_user_command and file.
