# semantic_search_exps.py — line-by-line analysis

## Lines 1-8
- Test script header and imports for JSON, OS, random, timing, and typing.

## Lines 9-16
- Imports numpy/tqdm plus embeddings/vectorstore dependencies.

## Lines 17-24
- Imports RoutingEngine/settings and defines data file locations.

## Lines 25-32
- Defines test case/embedding file paths and processed cases file.

## Lines 33-40
- Defines results paths and sets fixed random seed.

## Lines 41-48
- Commented size-range presets for registry selection.

## Lines 49-56
- Defines active SIZE_RANGES list with a single size bracket.

## Lines 57-64
- Completes SIZE_RANGES and starts load_agent_cards.

## Lines 65-72
- Validates agent cards directory and collects sorted JSON files.

## Lines 73-80
- Loads agent card JSON files and handles parse/read errors.

## Lines 81-88
- Logs count and returns agent cards; starts load_queries_and_responses.

## Lines 89-96
- load_queries_and_responses docstring describing inputs/returns.

## Lines 97-104
- Validates queries directory, gathers query JSON files, loops.

## Lines 105-112
- Loads each query file and handles JSON/read errors.

## Lines 113-120
- Logs query count, returns list, and begins prepare_agent_card.

## Lines 121-128
- Appends skill names/descriptions into a text representation.

## Lines 129-136
- Defines build_vecstore_from_vecs and validates vectors count.

## Lines 137-144
- Builds FAISS vectorstore from embeddings and metadata.

## Lines 145-152
- Starts compute_agent_card_embeddings and builds documents list.

## Lines 153-160
- Returns embedded documents and defines load_registries.

## Lines 161-168
- Loads registries file and defines load_test_cases.

## Lines 169-176
- Loads test cases JSON and defines load_agent_card_by_filename.

## Lines 177-184
- Loads single agent card JSON and starts load_query_response.

## Lines 185-192
- Loads query/response pair and returns agent/query/response dict.

## Lines 193-200
- select_registries_by_size_ranges docstring and RNG seed.

## Lines 201-208
- Computes registries in size range and builds candidate indices.

## Lines 209-216
- Samples indices per range and accumulates selection.

## Lines 217-224
- Logs selection stats and returns indices; starts get_test_cases_for_registry.

## Lines 225-232
- Filters test cases for a given registry.

## Lines 233-240
- load_turn_data docstring and argument descriptions.

## Lines 241-248
- Extracts agent/query indices and filenames from registry/test data.

## Lines 249-256
- Loads agent card and query response, asserts matching names.

## Lines 257-264
- Returns turn dict with agent name and human/AI messages.

## Lines 265-272
- load_testcase_data builds conversation list per testcase.

## Lines 273-280
- Appends turns and returns conversation/turn count dict.

## Lines 281-288
- get_agent_card_index_from_filename extracts numeric ID.

## Lines 289-296
- load_agent_cards_for_registry docstring and setup list.

## Lines 297-304
- Loads each registry agent card and returns list.

## Lines 305-312
- Defines build_vectorstore_for_registry signature and args.

## Lines 313-320
- Docstring describes registry vectorstore creation.

## Lines 321-328
- Builds registry card/embedding lists from agent entries.

## Lines 329-336
- Maps filenames to indices and builds vectorstore from vectors.

## Lines 337-344
- get_size_range_for_registry returns matching range or unknown.

## Lines 345-352
- load_processed_cases returns saved progress or defaults.

## Lines 353-360
- save_processed_cases writes progress JSON file.

## Lines 361-368
- semantic_search_exps loads registries/test cases and selects sample.

## Lines 369-376
- Saves sampled registries list and loads agent cards.

## Lines 377-384
- Computes embeddings if missing and saves to disk.

## Lines 385-392
- Loads embeddings from file and logs count.

## Lines 393-400
- Builds embeddings model and ensures results directory exists.

## Lines 401-408
- Initializes tracking counters for shortlist statistics.

## Lines 409-416
- Initializes routing engine and prepares shortlists output file.

## Lines 417-424
- Writes shortlists header and starts registry loop.

## Lines 425-432
- Reads registry size and computes size range.

## Lines 433-440
- Builds vectorstore and loads registry agent cards.

## Lines 441-448
- Retrieves test cases and writes registry header to file.

## Lines 449-456
- Iterates test cases, initializes conversation history and timers.

## Lines 457-464
- Writes test case header and iterates each turn query.

## Lines 465-472
- Calls router.route_query with message/history/cards/vectorstore.

## Lines 473-480
- Completes router call, times turn, and flags failures.

## Lines 481-488
- Writes turn header, user message, and correct agent info.

## Lines 489-496
- Writes shortlist details, similarity scores, and flushes output.

## Lines 497-504
- Writes PASS/FAIL status and separates turns.

## Lines 505-512
- Updates failure counters and shortlist presence flags.

## Lines 513-520
- Increments failure stats and begins exception handling.

## Lines 521-528
- Logs routing errors and writes failure details to file.

## Lines 529-536
- Appends human/assistant messages to conversation history.

## Lines 537-544
- Writes average turn time for test case and adds spacing.

## Lines 545-552
- Adds registry spacing and closes shortlists file.

## Lines 553-560
- Prints summary header and overall failed-turn stats.

## Lines 561-568
- Prints detailed failure breakdowns.

## Lines 569-576
- Handles no-failure case and prepares results filename.

## Lines 577-584
- Writes stats header and total/failed counts to results file.

## Lines 585-592
- Writes detailed failure breakdowns when failures exist.

## Lines 593-600
- Prints results filepath and returns stats dict.

## Lines 601-608
- Returns stats fields and starts __main__ block.

## Lines 609-616
- Commented-out embedding generation example code.

## Lines 617-620
- Calls semantic_search_exps in __main__.
