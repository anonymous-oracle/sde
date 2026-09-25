# start.sh — line-by-line analysis

## Lines 1-8
- Bash shebang, exit-on-error, startup message, and color constants.

## Lines 9-16
- Defines log_info helper to print blue INFO messages.

## Lines 17-24
- Defines log_success and log_warning helpers for green/yellow output.

## Lines 25-32
- Defines log_error helper and checks Docker availability.

## Lines 33-40
- Exits if Docker is down; starts agents-net network creation.

## Lines 41-48
- Logs network status and starts Kong with docker-compose.

## Lines 49-56
- Begins waiting loop for Kong health endpoint readiness.

## Lines 57-64
- Polls Kong status, prints dots, and increments attempts.

## Lines 65-72
- Handles Kong timeout failure and exits with log hints.

## Lines 73-80
- Starts wait loop for service registry readiness.

## Lines 81-88
- Polls registry health and increments attempts.

## Lines 89-96
- Logs registry timeout warning and starts chat history wait.

## Lines 97-104
- Polls chat history health and increments attempts.

## Lines 105-112
- Warns on chat history timeout and begins plugin configuration.

## Lines 113-120
- Queries existing chat-logger plugin and decides install path.

## Lines 121-128
- Sends POST to install plugin with chat service URL and timeout.

## Lines 129-136
- Captures HTTP code and logs success with plugin ID.

## Lines 137-144
- Logs install failure response and cleans temp response file.

## Lines 145-152
- Logs existing plugin and prints access point header lines.

## Lines 153-160
- Prints access URLs and shows usage example header.

## Lines 161-168
- Prints direct vs Kong route examples and monitoring header.

## Lines 169-176
- Prints service and route monitoring endpoints plus plugin list.

## Lines 177-184
- Prints next steps guidance for agent discovery and routing.

## Lines 185-185
- Final trailing echo.
