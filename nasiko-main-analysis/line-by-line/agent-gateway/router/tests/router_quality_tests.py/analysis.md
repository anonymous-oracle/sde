# router_quality_tests.py — line-by-line analysis

## Lines 1-8
- Imports modules and test dependencies.

## Lines 9-16
- Imports modules and test dependencies.

## Lines 17-24
- Defines configuration or data variables: AGENT_CARDS_DIR, QUERIES_RESPONSES_DIR, REGISTRIES_FILE.

## Lines 25-32
- Defines configuration or data variables: FAILURES_DIR, RESULTS_FILE, RANDOM_SEED.

## Lines 33-40
- Commented-out notes or test data.

## Lines 41-48
- Defines configuration or data variables: SIZE_RANGES.

## Lines 49-56
- Defines function(s) load_agent_cards with conditionals.

## Lines 57-64
- Defines configuration or data variables: json_files, key, agent_cards.

## Lines 65-72
- Defines configuration or data variables: agent_card.

## Lines 73-80
- Defines function(s) load_queries_and_responses with returns.

## Lines 81-88
- Defines configuration or data variables: queries_and_responses_path.

## Lines 89-96
- Defines configuration or data variables: json_files, queries.

## Lines 97-104
- Defines configuration or data variables: query.

## Lines 105-112
- Defines function(s) prepare_agent_card with loops.

## Lines 113-120
- Defines function(s) build_vecstore_from_vecs with returns.

## Lines 121-128
- Defines configuration or data variables: texts, text_embedding_pairs, metadatas.

## Lines 129-136
- Defines configuration or data variables: vector_store.

## Lines 137-144
- Defines function(s) compute_agent_card_embeddings with loops, returns.

## Lines 145-152
- Defines function(s) load_registries, load_test_cases with returns.

## Lines 153-160
- Defines function(s) load_agent_card_by_filename with returns.

## Lines 161-168
- Defines function(s) load_query_response with loops, returns.

## Lines 169-176
- Defines configuration or data variables: data, query_response.

## Lines 177-184
- Defines function(s) select_registries_by_size_ranges with error handling.

## Lines 185-192
- Defines configuration or data variables: selected_indices, indices_in_range.

## Lines 193-200
- Defines configuration or data variables: num_to_select, selected.

## Lines 201-208
- Continues test logic and data handling.

## Lines 209-216
- Defines function(s) get_test_cases_for_registry with loops, conditionals, error handling, returns.

## Lines 217-224
- Defines function(s) load_turn_data with error handling.

## Lines 225-232
- Defines configuration or data variables: agent_idx, query_index, agent_entry.

## Lines 233-240
- Defines configuration or data variables: agent_card_filename, query_filename, agent_card.

## Lines 241-248
- Assertions and validation checks.

## Lines 249-256
- Defines function(s) load_testcase_data with error handling.

## Lines 257-264
- Defines configuration or data variables: conversation, query_data.

## Lines 265-272
- Defines function(s) get_agent_card_index_from_filename with returns.

## Lines 273-280
- Defines function(s) load_agent_cards_for_registry with loops, error handling.

## Lines 281-288
- Defines configuration or data variables: registry_agent_cards, agent_card_filename, agent_card.

## Lines 289-296
- Defines function(s) build_vectorstore_for_registry with error handling, returns.

## Lines 297-304
- Loop logic for processing test data.

## Lines 305-312
- Defines configuration or data variables: registry_agent_cards, registry_embeddings.

## Lines 313-320
- Defines configuration or data variables: agent_card_filename, agent_card_idx.

## Lines 321-328
- Defines function(s) get_size_range_for_registry with loops, conditionals, error handling.

## Lines 329-336
- Defines function(s) load_processed_cases with conditionals, returns.

## Lines 337-344
- Defines function(s) save_processed_cases with error handling, returns.

## Lines 345-352
- Defines function(s) test_router_quality.

## Lines 353-360
- Defines configuration or data variables: selected_registry_indices.

## Lines 361-368
- Defines configuration or data variables: agent_cards.

## Lines 369-376
- Defines configuration or data variables: agent_cards_embeddings.

## Lines 377-384
- Defines configuration or data variables: agent_cards_embeddings, embeddings_model.

## Lines 385-392
- Defines configuration or data variables: processed_cases.

## Lines 393-400
- Defines configuration or data variables: completed_registry_indices, registries_to_process.

## Lines 401-408
- Loop logic for processing test data.

## Lines 409-416
- Defines configuration or data variables: total_turns, failed_turns, total_convs.

## Lines 417-424
- Defines configuration or data variables: stats_by_size_range.

## Lines 425-432
- Defines configuration or data variables: turn_idx_stats, router.

## Lines 433-440
- Defines configuration or data variables: registry, registry_size, size_range.

## Lines 441-448
- Defines configuration or data variables: vectorstore, registry_agent_cards.

## Lines 449-456
- Defines configuration or data variables: registry_test_cases, conversation_history, conv_failed.

## Lines 457-464
- Defines configuration or data variables: turn_data.

## Lines 465-472
- Continues test logic and data handling.

## Lines 473-480
- Defines configuration or data variables: message, conversation_history.

## Lines 481-488
- Defines configuration or data variables: agent_cards, vectorstore, selected_agent.

## Lines 489-496
- Defines configuration or data variables: conv_failed.

## Lines 497-504
- Continues test logic and data handling.

## Lines 505-512
- Continues test logic and data handling.

## Lines 513-520
- Defines configuration or data variables: conv_failed.

## Lines 521-528
- Continues test logic and data handling.

## Lines 529-536
- Continues test logic and data handling.

## Lines 537-544
- Defines configuration or data variables: all_turns_data, td.

## Lines 545-552
- Continues test logic and data handling.

## Lines 553-560
- Defines configuration or data variables: failure_data.

## Lines 561-568
- Defines configuration or data variables: failure_filename, failure_path.

## Lines 569-576
- Continues test logic and data handling.

## Lines 577-584
- Conditional logic for branching test cases.

## Lines 585-592
- Conditional logic for branching test cases.

## Lines 593-600
- Defines configuration or data variables: stats.

## Lines 601-608
- Defines configuration or data variables: turn_acc, conv_acc.

## Lines 609-616
- Conditional logic for branching test cases.

## Lines 617-624
- Continues test logic and data handling.

## Lines 625-632
- Defines configuration or data variables: stats, acc.

## Lines 633-640
- Continues test logic and data handling.

## Lines 641-648
- Conditional logic for branching test cases.

## Lines 649-656
- Continues test logic and data handling.

## Lines 657-664
- Continues test logic and data handling.

## Lines 665-672
- Commented-out notes or test data.

## Lines 673-680
- Commented-out notes or test data.

## Lines 681-688
- Commented-out notes or test data.

## Lines 689-696
- Commented-out notes or test data.

## Lines 697-704
- Commented-out notes or test data.

## Lines 705-712
- Commented-out notes or test data.

## Lines 713-720
- Commented-out notes or test data.

## Lines 721-728
- Commented-out notes or test data.

## Lines 729-736
- Commented-out notes or test data.

## Lines 737-744
- Commented-out notes or test data.

## Lines 745-752
- Commented-out notes or test data.

## Lines 753-760
- Commented-out notes or test data.

## Lines 761-768
- Commented-out notes or test data.

## Lines 769-776
- Conditional logic for branching test cases.

## Lines 777-784
- Commented-out notes or test data.

## Lines 785-787
- Continues test logic and data handling.
