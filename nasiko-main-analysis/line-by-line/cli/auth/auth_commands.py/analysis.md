# auth_commands.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports typer, Optional, sys, and os.

## Lines 9-16
- Extends sys.path, imports auth manager/api client, and defines auth_app.

## Lines 17-24
- Declares login_command and access_key option configuration.

## Lines 25-32
- Adds access_secret, save_credentials, and api_url options.

## Lines 33-40
- Login docstring and prompts for missing access key.

## Lines 41-48
- Prompts for access secret and validates required inputs.

## Lines 49-56
- Validates key prefix and configures auth_manager base_url.

## Lines 57-64
- Attempts login and fetches user info on success.

## Lines 65-72
- Prints welcome/command hints or exits on login failure.

## Lines 73-80
- Defines logout_command with clear_all option and auth manager fetch.

## Lines 81-88
- Handles not-logged-in case and logout success messages.

## Lines 89-96
- Prints credential clearing or warning on logout failure.

## Lines 97-104
- Defines status_command and checks login state.

## Lines 105-112
- Prints user info fields when available.

## Lines 113-120
- Prints last login and begins API connectivity test.

## Lines 121-128
- Checks healthcheck endpoint and prints API status.

## Lines 129-136
- Handles not-logged-in output and login hint.

## Lines 137-144
- Defines whoami_command and handles not-logged-in case.

## Lines 145-152
- Fetches user info and reports missing data errors.

## Lines 153-160
- Prints username/email/role/active status.

## Lines 161-168
- Prints created/last login fields when present.

## Lines 169-176
- Defines login_standalone wrapper and delegates to _do_login.

## Lines 177-184
- Defines _do_login signature and validates inputs.

## Lines 185-192
- Validates key format and configures auth_manager auth_url.

## Lines 193-200
- Attempts login and prints welcome on success.

## Lines 201-208
- Raises exit on failure and ends helper.

## Lines 209-216
- __main__ guard to run auth_app CLI.

## Lines 217-218
- End of file.
