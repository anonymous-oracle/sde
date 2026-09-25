# docker_utils.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports subprocess/time/logging, and sets logger.

## Lines 9-16
- Defines run_cmd to log and execute subprocess commands.

## Lines 17-24
- Begins wait_for_health, logs wait, and starts timeout loop.

## Lines 25-32
- Runs docker inspect, checks status, logs running, sleeps between checks.

## Lines 33-40
- Logs timeout failure and begins get_container_host_port docstring.

## Lines 41-48
- Explains deprecation, calls docker port, and logs mapping.

## Lines 49-56
- Parses port mapping and returns localhost URL or fallback.

## Lines 57-64
- Logs missing mapping, handles subprocess errors, and returns fallback URL.

## Lines 65-72
- Starts get_kong_agent_url with docstring and socket import.

## Lines 73-80
- Determines private IP via UDP socket and handles exceptions.

## Lines 81-88
- Logs fallback to localhost, builds Kong URL, and logs it.

## Lines 89-96
- Returns Kong URL and starts network_exists helper.

## Lines 97-104
- Runs docker network ls command to check for network presence.

## Lines 105-112
- Returns network existence or false on subprocess error.

## Lines 113-120
- Starts create_network and checks for existing network.

## Lines 121-128
- Creates network, logs result, handles errors, or logs already exists.

## Lines 129-130
- Returns final boolean result.
