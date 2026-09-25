# redisclient.py — line-by-line analysis

## Lines 1-8
- Imports redis/os, reads host/port env vars, and defines get_redis_client.

## Lines 9-16
- set_github_access_token writes token to Redis key.

## Lines 17-25
- get_github_access_token reads/decodes token and clear_github_access_token deletes it.
