# redis_search_service.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for Redis asyncio, typing, logging, and os.

## Lines 9-16
- Imports json/datetime/re and declares RedisSearchService with docstring.

## Lines 17-24
- __init__ sets logger and reads Redis host/URL from environment.

## Lines 25-32
- Creates Redis client and sets hash prefixes plus username/email index keys.

## Lines 33-40
- Defines role/active/all user keys and agent index key prefixes.

## Lines 41-48
- Finishes agent index keys and starts _check_connection with ping.

## Lines 49-56
- Logs connection errors and initialize warns when Redis unavailable.

## Lines 57-64
- Returns False on unavailable; logs success and starts _serialize_for_redis.

## Lines 65-72
- Initializes serialized dict and handles None/datetime conversion.

## Lines 73-80
- Serializes dict/list/bool/other values and returns serialized mapping.

## Lines 81-88
- _deserialize_from_redis starts, returns empty on no data, init dict.

## Lines 89-96
- Iterates items, decodes bytes, and begins empty-string-to-None handling.

## Lines 97-104
- Maps empty fields to None and parses boolean string values.

## Lines 105-112
- Parses tags JSON with fallback or stores raw value.

## Lines 113-120
- Returns deserialized data; normalize_query and create_search_tokens start.

## Lines 121-128
- Handles empty text, normalizes query, initializes tokens, and adds full text.

## Lines 129-136
- Adds word tokens and starts prefix generation for autocomplete.

## Lines 137-144
- Generates prefixes, dedupes tokens, and starts _calculate_match_score signature.

## Lines 145-152
- Returns 0 for empty inputs and normalizes query/text.

## Lines 153-160
- Exact match and prefix match scoring logic.

## Lines 161-168
- Contains match scoring and word boundary checks.

## Lines 169-176
- Returns lower scores for word matches, else 0; search_users signature begins.

## Lines 177-184
- Checks connection, normalizes query, and returns early for short queries.

## Lines 185-192
- Loads active users set, handles empty, and initializes user_scores list.

## Lines 193-200
- Iterates user IDs, decodes bytes, and fetches user hash data.

## Lines 201-208
- Skips missing user data and decodes hash keys/values to strings.

## Lines 209-216
- Calculates username and display_name match scores with boosts.

## Lines 217-224
- Calculates email score and computes total_score.

## Lines 225-232
- Stores score for matches and sorts by score/username.

## Lines 233-240
- Limits results and returns users/total/max_score payload.

## Lines 241-248
- Logs search error and starts search_agents signature.

## Lines 249-256
- Checks connection, normalizes query, and handles short queries.

## Lines 257-264
- Loads all agents set, handles empty, initializes agent_scores list.

## Lines 265-272
- Iterates agent IDs, decodes bytes, and fetches agent hash data.

## Lines 273-280
- Skips missing agent data and decodes hash keys/values.

## Lines 281-288
- Calculates agent_id/name/description match scores with boosts.

## Lines 289-296
- Initializes tag_score and attempts to parse tags for scoring.

## Lines 297-304
- Assigns high score for exact tag match and partial match fallback.

## Lines 305-312
- Computes total_score and begins matched-agent response handling.

## Lines 313-320
- Parses tags list for response, assigns score, and appends to results.

## Lines 321-328
- Sorts by score/name and limits results for response.

## Lines 329-336
- Returns agents/total/max_score and handles exceptions.

## Lines 337-344
- Logs agent search error and begins index_user method.

## Lines 345-352
- Checks connection, extracts user_id, and serializes user data.

## Lines 353-360
- Stores user hash and adds user to general index set.

## Lines 361-368
- Updates active users set based on is_active flag.

## Lines 369-376
- Adds user to role index, logs, and returns True.

## Lines 377-384
- Logs indexing error and starts index_agent method.

## Lines 385-392
- Checks connection, extracts agent_id, and serializes agent data.

## Lines 393-400
- Stores agent hash and adds agent to general index.

## Lines 401-408
- Adds agent to owner index when owner_id present.

## Lines 409-416
- Adds agent to tag indexes using normalized tag values.

## Lines 417-424
- Logs indexed agent and handles errors with False return.

## Lines 425-432
- Logs index_agent error and starts delete_user method.

## Lines 433-440
- Checks connection, fetches user data, deletes hash, and removes from sets.

## Lines 441-448
- Decodes user data and removes user from role index.

## Lines 449-456
- Logs deletion and returns True; handles delete_user errors.

## Lines 457-464
- Logs deletion error and starts delete_agent method.

## Lines 465-472
- Checks connection, fetches agent data, deletes hash, and removes from all set.

## Lines 473-480
- Decodes agent data and prepares to remove owner index entry.

## Lines 481-488
- Removes from owner index and begins tag index cleanup.

## Lines 489-496
- Parses tags list and removes agent from tag indexes.

## Lines 497-504
- Logs deletion, returns True, and handles errors.

## Lines 505-512
- Logs delete_agent error and starts bulk_index_users.

## Lines 513-520
- Checks connection/users, indexes each user, and counts success.

## Lines 521-528
- Logs count, returns success_count, and handles errors.

## Lines 529-536
- Starts bulk_index_agents, checks connection, and loops agents.

## Lines 537-544
- Logs count/returns and handles bulk indexing errors.

## Lines 545-552
- Logs error and starts clear_all_indexes with connection check.

## Lines 553-560
- Defines key patterns and scans keys for each pattern.

## Lines 561-568
- Deletes matched keys, logs success, and returns True.

## Lines 569-574
- Logs failure and returns False on exceptions.
