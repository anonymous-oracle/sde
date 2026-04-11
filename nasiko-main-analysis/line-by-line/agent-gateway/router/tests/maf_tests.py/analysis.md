# maf_tests.py — line-by-line analysis

## Lines 1-8
- Test script header and imports for JSON/OS/random/time/types.

## Lines 9-16
- Imports numpy/tqdm and embeddings/vectorstore helpers.

## Lines 17-24
- Imports RoutingEngine/settings and defines MAF data directories.

## Lines 25-32
- Defines MAF registries/testcases/embeddings files.

## Lines 33-40
- Defines results paths and processed cases file.

## Lines 41-48
- Sets random seed and begins size range presets.

## Lines 49-56
- Commented size range presets.

## Lines 57-64
- Defines active SIZE_RANGES and ends list.

## Lines 65-72
- load_agent_cards validates directory and gathers agent_card JSONs.

## Lines 73-80
- Loads agent cards and handles JSON/read errors.

## Lines 81-88
- Logs card count and returns list; begins load_queries_and_responses.

## Lines 89-96
- load_queries_and_responses docstring and path validation.

## Lines 97-104
- Handles missing queries dir and prepares to load files.

## Lines 105-112
- Loads query JSON files and handles parsing errors.

## Lines 113-120
- Logs query count and returns list.

## Lines 121-128
- prepare_agent_card builds text for name/description/skills.

## Lines 129-136
- Finishes skill text, returns, and starts build_vecstore_from_vecs.

## Lines 137-144
- Validates vector sizes and prepares embedding pairs/metadata.

## Lines 145-152
- Builds FAISS store and returns it.

## Lines 153-160
- compute_agent_card_embeddings builds docs list and embeds.

## Lines 161-168
- load_registries reads MAF registries JSON.

## Lines 169-176
- load_test_cases reads test cases and defines load_agent_card_by_filename.

## Lines 177-184
- Loads single agent card JSON and defines load_maf_idea_by_filename.

## Lines 185-192
- Loads MAF idea JSON and starts load_maf_test_queries.

## Lines 193-200
- load_maf_test_queries docstring and args.

## Lines 201-208
- Loads MAF queries file and returns query set pairs.

## Lines 209-216
- load_query_response loads query/response pair for agent.

## Lines 217-224
- Returns agent/query/response dict and starts select_registries_by_size_ranges.

## Lines 225-232
- Selection docstring, seeds RNG, initializes list.

## Lines 233-240
- Computes indices by actual_size and builds candidate list.

## Lines 241-248
- Samples indices per range and logs selection stats.

## Lines 249-256
- Returns selected registry indices and starts get_test_cases_for_registry.

## Lines 257-264
- Filters MAF test cases for registry and samples up to 5.

## Lines 265-272
- load_maf_test_case_data docstring and returns description.

## Lines 273-280
- Loads MAF query set and returns maf_name/file/queries.

## Lines 281-288
- Ends load_maf_test_case_data and starts load_turn_data.

## Lines 289-296
- load_turn_data docstring and args for agent/registry.

## Lines 297-304
- Resolves agent card filename and loads agent card.

## Lines 305-312
- Loads query response and asserts agent name matches.

## Lines 313-320
- Returns turn dict with agent name and messages.

## Lines 321-328
- load_testcase_data builds conversation for standard test cases.

## Lines 329-336
- Returns conversation/turn count and defines index helper.

## Lines 337-344
- get_agent_card_index_from_filename extracts numeric ID.

## Lines 345-352
- load_agent_cards_for_registry docstring and setup.

## Lines 353-360
- Loads agent cards across all MAFs in registry.

## Lines 361-368
- Starts build_vectorstore_for_registry and arguments.

## Lines 369-376
- Docstring describes building vectorstore across MAF agents.

## Lines 377-384
- Initializes registry card/embedding lists and loops mafs.

## Lines 385-392
- Loads MAF idea agents and collects embeddings.

## Lines 393-400
- Builds vectorstore from collected cards/embeddings.

## Lines 401-408
- get_size_range_for_registry helper and load_processed_cases.

## Lines 409-416
- Loads processed cases from file or defaults.

## Lines 417-424
- save_processed_cases writes progress JSON and starts semantic_search_exps.

## Lines 425-432
- Loads registries/test cases and selects sampled registries.

## Lines 433-440
- Saves sampled registry indices, prints count, loads agent cards.

## Lines 441-448
- Computes embeddings if missing and saves to disk.

## Lines 449-456
- Loads embeddings from file and logs count.

## Lines 457-464
- Builds embeddings model for vectorstore.

## Lines 465-472
- Creates results directory and initializes failure counters.

## Lines 473-480
- Initializes routing engine and opens shortlists file.

## Lines 481-488
- Writes shortlists header and begins registry loop.

## Lines 489-496
- Reads registry actual_size and builds vectorstore.

## Lines 497-504
- Loads registry agent cards/test cases and writes header.

## Lines 505-512
- Starts MAF test loop, names test, and writes header.

## Lines 513-520
- Loads MAF queries and handles load errors.

## Lines 521-528
- Prints query count and iterates each query turn.

## Lines 529-536
- Extracts user message/agent/response and increments counters.

## Lines 537-544
- Calls router.route_query for each turn.

## Lines 545-552
- Completes router call, times turn, appends time.

## Lines 553-560
- Writes user/correct agent info to shortlist output.

## Lines 561-568
- Writes shortlist details and flushes output.

## Lines 569-576
- Writes PASS/FAIL status lines.

## Lines 577-584
- Updates failure counters based on shortlist membership.

## Lines 585-592
- Logs routing errors and writes failed turn info.

## Lines 593-600
- Appends conversation history entries for turns.

## Lines 601-608
- Writes average turn time per test case.

## Lines 609-616
- Adds spacing between test cases and closes file after loop.

## Lines 617-624
- Prints shortlist stats header and total failed counts.

## Lines 625-632
- Prints failure breakdown percentages.

## Lines 633-640
- Prints no-failure case and prepares results file.

## Lines 641-648
- Writes stats header and total/failed counts to results file.

## Lines 649-656
- Writes failure breakdowns to file when needed.

## Lines 657-664
- Prints results file path and returns stats dict.

## Lines 665-672
- Returns stats fields and starts __main__ block.

## Lines 673-680
- Commented-out embedding generation example.

## Lines 681-688
- Commented-out embedding save/load lines.

## Lines 689-690
- Calls semantic_search_exps in __main__.
